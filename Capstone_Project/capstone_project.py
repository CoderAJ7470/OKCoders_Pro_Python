#!/usr/bin/env python

"""
Capstone Project

Scrape latest five posts from the Hackernews site (every morning at 10:00 Central)
Read all posts into a database
Send an email with all five posts and their respective links
Optionally send a ntfy push notification
"""

import ezgmail
import os
import requests
import sqlite3
import time
from decouple import config
from pathlib import Path

# Environment Variables
BASE_DIR = Path(__file__).resolve().parent
EMAIL = config("EMAIL", default="aj1710m@gmail.com")

# Database path
db_path = BASE_DIR / 'capstone_hn_posts.db'


def get_latest_five_posts():
    base_item_url = 'https://hacker-news.firebaseio.com/v0/item/{}.json'

    # Fetch story IDs with retry logic
    max_retries = 3
    retry_delay = 1
    ids = []

    print('Fetching latest stories from Hacker News...')
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json', timeout=10)
            ids = response.json()[:5]
            print(f'Retrieved {len(ids)} story IDs')
            break
        except requests.exceptions.Timeout:
            print(f'Timeout on attempt {attempt}/{max_retries} fetching story list')
            if attempt < max_retries:
                time.sleep(retry_delay)
            else:
                print(f'Failed to fetch story list after {max_retries} attempts')
                return
        except requests.exceptions.RequestException as e:
            print(f'Error on attempt {attempt}/{max_retries}: {e}')
            if attempt < max_retries:
                time.sleep(retry_delay)
            else:
                print(f'Failed to fetch story list after {max_retries} attempts')
                return

    if not ids:
        print('No story IDs retrieved')
        return

    posts = []

    for i, story_id in enumerate(ids, 1):
        print(f'Fetching story {i}/{len(ids)} (ID: {story_id})...')
        # Try up to 3 times with shorter timeout
        max_retries = 3
        retry_delay = 1
        story = None

        for attempt in range(1, max_retries + 1):
            try:
                story_response = requests.get(base_item_url.format(story_id), timeout=5)
                story = story_response.json()

                # Check if API returned null
                if story is None:
                    if attempt < max_retries:
                        print('  API returned null, retrying...')
                        time.sleep(retry_delay)
                        continue
                    else:
                        print(f'  API returned null after {max_retries} attempts, skipping')
                        break

                break  # Success, exit retry loop
            except requests.exceptions.Timeout:
                if attempt < max_retries:
                    print(f'  Timeout on attempt {attempt}, retrying...')
                    time.sleep(retry_delay)
                else:
                    print(f'  Timeout after {max_retries} attempts, skipping')
                    continue
            except requests.exceptions.RequestException as e:
                if attempt < max_retries:
                    print(f'  Error: {e}, retrying...')
                    time.sleep(retry_delay)
                else:
                    print(f'  Error after {max_retries} attempts, skipping')
                    continue

        # Only add if we successfully got the story
        if story:
            posts.append(
                {
                    'story_id': story_id,
                    'title': story.get('title', 'No title'),
                    'url': story.get('url', f'https://news.ycombinator.com/item?id={story_id}'),
                    'by': story.get('by', 'unknown'),
                    'time': story.get('time', 0),
                }
            )
            print(f'  ✓ {story.get("title")}')

    if posts:
        print(f'\nSuccessfully fetched {len(posts)} posts')
        read_posts_into_db(posts)
        print('Posts stored in database!')
    else:
        print('\nNo posts were successfully fetched')


def read_posts_into_db(posts):
    posts_db = sqlite3.connect(db_path, isolation_level=None)
    cursor = posts_db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS latest_posts (
            story_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            link TEXT,
            posted_by TEXT,
            posted_time INTEGER
        )
    ''')

    for post in posts:
        cursor.execute(
            '''
            INSERT OR REPLACE INTO latest_posts (story_id, title, link, posted_by, posted_time)
            VALUES (?, ?, ?, ?, ?)
        ''',
            (post['story_id'], post['title'], post['url'], post['by'], post['time']),
        )

    posts_db.close()


def print_movie_db():
    movie_db = sqlite3.connect(db_path, isolation_level=None)
    rows = movie_db.execute('SELECT * FROM latest_posts').fetchall()

    for row in rows:
        print(row)  # prints each tuple (row) in the db

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
    cursor.execute('SELECT title, link, posted_by, posted_time FROM latest_posts ORDER BY story_id DESC LIMIT 5')
    rows = cursor.fetchall()
    conn.close()

    # Formatting the email body
    email_body = 'Here are the latest 5 Hacker News posts:\n\n'
    for i, (title, link, posted_by, _) in enumerate(rows, start=1):
        email_body += f'{i}. {title}\n'
        email_body += f'   Posted by: {posted_by}\n'
        email_body += f'   Link: {link}\n\n'

    print(f'Sending email to {EMAIL}...')
    ezgmail.send(EMAIL, 'Latest Five HN Posts', email_body)
    print('Email sent successfully!')


def main():
    get_latest_five_posts()
    send_posts_through_email()


if __name__ == '__main__':
    main()
