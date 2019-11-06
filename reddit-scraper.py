import praw
import pandas as pd
import json

# Get PRAW and Reddit credentials from config.json
app_name = ''
praw_personal_use_script = ''
praw_key = ''
reddit_username = ''
reddit_password = ''
try:
    with open('config.json') as f:
        config = json.load(f)
        app_name = config['App name']
        praw_personal_use_script = config['PRAW personal use script']
        praw_key = config['PRAW key']
        reddit_username = config['Reddit username']
        reddit_password = config['Reddit password']
except json.decoder.JSONDecodeError as e:
    print(e)

# Setup Reddit instance
reddit = praw.Reddit(client_id=praw_personal_use_script, client_secret=praw_key, user_agent=app_name, username=reddit_username, password=reddit_password)
subreddit = reddit.subreddit('yorku')

# Scrape posts and export
top_submissions = {'title': [], 'body': []}

for submissions in subreddit.top(limit=100):
    top_submissions['title'].append(submissions.title)
    top_submissions['body'].append(submissions.selftext)

data = pd.DataFrame.from_dict(top_submissions)

data.to_csv('data/reddit_submissions.csv')
