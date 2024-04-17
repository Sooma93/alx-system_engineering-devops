#!/usr/bin/python3
"""
api rediernt
"""

import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyBot/1.0'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
