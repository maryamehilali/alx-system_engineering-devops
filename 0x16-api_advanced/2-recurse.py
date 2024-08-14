#!/usr/bin/python3
"""
This module contains a cursive function that queries the Reddit API
and returns a list containing the titles of all hot articles for
a given subreddit. If no results are found for the given subreddit,
the function should return None.
"""
import requests


url = "https://www.reddit.com"
headers = {
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }


def recurse(subreddit, hot_list=[], after=None):
    """Function definition"""
    if after is not None:
        resp = requests.get(
            '{}/r/{}/hot.json?after={}'.format(url, subreddit, after),
            headers=headers, allow_redirects=False
            )
    else:
        resp = requests.get(
            '{}/r/{}/hot.json'.format(url, subreddit),
            headers=headers, allow_redirects=False
            )
    if resp.status_code == 200:
        data = resp.json().get('data', {})
        posts = data.get('children', [])

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
