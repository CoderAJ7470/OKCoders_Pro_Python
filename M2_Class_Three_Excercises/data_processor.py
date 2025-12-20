# Build a data processing system that does the following:

# Scrapes data from a website
# Processes the data in a database
# Generates a report with charts
# Emails report to recipients with EZGmail
# Sends a push notification when done with ntfy

import requests, bs4, sqlite3

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
    
def read_posts_into_db():
    posts_db = sqlite3.connect('hn_posts.db', isolation_level = None)
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

    posts_db.close()

get_latest_five_posts()