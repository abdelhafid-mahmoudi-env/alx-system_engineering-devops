#!/usr/bin/python3
"""
Contains the number_of_subscribers function,
which queries the Reddit API and retrieves
the number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subscribers
    and returns the count.
    """
    u_agent = 'Mozilla/5.0'
    headers = {'User-Agent': u_agent}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    dic = res.json()
    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0
    return res.json()['data']['subscribers']
