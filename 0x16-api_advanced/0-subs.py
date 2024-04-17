#!/usr/bin/python3
"""
api redient
"""

import requests


def number_of_subscribers(subreddit):
    """
    function redor=ent query
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url,  headers={"User-Agent": "Custom"})
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data').get('subscribers')
        return subscribers
    else:
        return 0
