# Capstone Project

# Scrape latest five posts from the Hackernews site (every morning at 10:00 Central)
# Read all posts into a database
# Send an email with all five posts and their respective links
# Optionally send a ntfy push notification

import requests, sqlite3, ezgmail, os
from pathlib import Path

# Since we are using VS Code, one of its quirks with Python files is that the full URL needs to be resolved to specify the exact location where you want to create the .db file, if it does not exist already. So this is why we are creating the full file path first before using it down in the read_posts_into_db function below
BASE_DIR = Path(__file__).resolve().parent
db_path = BASE_DIR / 'capstone_hn_posts.db'

def get_latest_five_posts():
    base_item_url = 'https://hacker-news.firebaseio.com/v0/item/{}.json'
    
    ids = requests.get(
        'https://hacker-news.firebaseio.com/v0/newstories.json'
    ).json()[:5]

    posts = []

    for story_id in ids:
        story = requests.get(base_item_url.format(story_id)).json()
        
        posts.append({
            'title': story.get('title'),
            'url': story.get('url'),
            'by': story.get('by'),
            'time': story.get('time')
        })

    print('Latest five posts: ', posts)
    
    read_posts_into_db(posts)
    
    print('Latest five posts stored successfully in database!')
    
def read_posts_into_db(posts):
    posts_db = sqlite3.connect(db_path, isolation_level = None)
    cursor = posts_db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS latest_posts (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            link TEXT,
            posted_by TEXT,
            posted_time INTEGER
        )
    ''')
    
    for post in posts:
        cursor.execute('''
            INSERT INTO latest_posts (title, link, posted_by, posted_time)
            VALUES (?, ?, ?, ?)
        ''', (post['title'], post['url'], post['by'], post['time']))

    posts_db.close()
    
def print_movie_db():
    movie_db = sqlite3.connect(db_path, isolation_level = None)
    rows = movie_db.execute('SELECT * FROM latest_posts').fetchall()
    
    for row in rows:
        print(row) # prints each tuple (row) in the db
        
    movie_db.close()

# Sends an email containing the latest five posts
def send_posts_through_email():
    # Ensure BASE_DIR is the folder where this script lives
    try:
        BASE_DIR = Path(__file__).resolve().parent
    except NameError:
        BASE_DIR = Path.cwd()

    # Force current working directory to script folder
    os.chdir(BASE_DIR)

    db_path_local = BASE_DIR / 'capstone_hn_posts.db'
    token_path = BASE_DIR / 'token.json'
    credentials_path = BASE_DIR / 'credentials.json'

    # Initialize ezgmail if token.json doesn't exist
    if not token_path.exists():
        ezgmail.init(credentialsFile=str(credentials_path))
    else:
        ezgmail.init()  # token.json exists, safe to init without credentialsFile

    # Fetch posts from the db
    conn = sqlite3.connect(db_path_local)
    cursor = conn.cursor()
    cursor.execute('SELECT title, link, posted_by, posted_time FROM latest_posts ORDER BY id DESC LIMIT 5')
    rows = cursor.fetchall()
    conn.close()

    # Formatting the email body
    email_body = 'Here are the latest 5 Hacker News posts:\n\n'
    for i, (title, link, posted_by, posted_time) in enumerate(rows, start=1):
        email_body += f'{i}. {title}\n'
        email_body += f'   Posted by: {posted_by}\n'
        email_body += f'   Link: {link}\n\n'

    ezgmail.send('aj1710m@gmail.com', 'Latest Five HN Posts', email_body)
    
    print('\nEmail sent successfully!\n')

    
def main():
    get_latest_five_posts()
    send_posts_through_email()

if __name__ == '__main__':
    main()

