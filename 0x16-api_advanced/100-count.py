#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count of
given keywords (case-insensitive, delimited by spaces. Javascript
should count as javascript, but java should not).
"""
import requests


url = "https://www.reddit.com"
headers = {
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }


def count_words(subreddit, word_list, counts={}, after=None):
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
    word_search = [word.lower() for word in word_list]
    counts = {word: 0 for word in word_list}
    if resp.status_code == 200:
        data = resp.json().get('data', {})
        posts = data.get('children', [])

        for post in posts:
            hot_list = post['data']['title']
            post_words = hot_list.split()
            post_words = [word.lower() for word in post_words]
            for word in word_search:
                counts[word] += post_words.count(word)

        after = data.get('after')
        if after:
            return count_words(subreddit, word_list, counts, after)
        else:
            sorted_counts = dict(sorted(counts.items(),
                                        key=lambda item: item[1],
                                        reverse=True))
            for key, value in sorted_counts.items():
                if value > 0:
                    print("{}: {}".format(key, value))
            return counts
    else:
        return None
