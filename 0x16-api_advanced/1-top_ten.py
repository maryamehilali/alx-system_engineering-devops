#!/usr/bin/python3
"""
This module contains a function that queries
the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Function definition"""
    url = "https://www.reddit.com"
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
    resp = requests.get(
        '{}/r/{}/.json?sort=top&limit=10'.format(url, subreddit),
        headers=headers, allow_redirects=False
        )
    if resp.status_code == 200:
        for post in resp.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
