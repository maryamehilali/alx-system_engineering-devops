#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Function definition"""
    url = "https://www.reddit.com"
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
    resp = requests.get(
        '{}/r/{}/about.json'.format(url, subreddit),
        headers=headers, allow_redirects=False
        )
    if resp.status_code == 200:
        return resp.json()['data']['subscribers']
    else:
        return 0
