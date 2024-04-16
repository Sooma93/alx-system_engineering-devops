#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit. If not valid subreddit, returns 0
"""
import requests


def number_of_subscribers(subreddit):
    try:
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/39.0.2171.95 Safari/537.36',
            'accept': 'application/json'}
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False).json()
        return response['data']['subscribers']
    except BaseException:
        return 0
