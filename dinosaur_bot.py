import praw
import config
import time
import os

# Authenticates the reddit account used by importing credentials from config.py
def authenticate():
    print('\n>>> Attempting to authenticate reddit credentials...\n')
    reddit = praw.Reddit(client_id = config.client_id,
						client_secret = config.client_secret,
						username = config.username,
						password = config.password,
						user_agent = config.user_agent)
    print('>>> Successfully authenticated as ' + str(reddit.user.me()) + '.')

    return reddit

# List containing comment ID's to disable replying to the same comment repeatedly
reply_list = []


def run_bot(reddit):  # Script that runs the actual bot
    print('\n>>> Obtaining the last 250 reddit comments...')
    for comment in reddit.subreddit('all').comments(limit=250):
        if 'dinosaur' in comment.body and comment.id not in reply_list and comment.author != reddit.user.me():
            try:
                print('\n>>> Comment found with identified string ' + comment.id)
                comment.reply("Hi, I'm a dinosaur.")
                print('>>> Comment successfully replied to ' + comment.id)
                reply_list.append(comment.id)
            except:
                print('\n>>>Not enough karma to comment, restarting bot...')
                run_bot(reddit)

    print('\n>>> Sleeping bot for 10 seconds...')
    time.sleep(10)

reddit = authenticate()

while True:  # Command to keep the script running until cancelled by user
    run_bot(reddit)