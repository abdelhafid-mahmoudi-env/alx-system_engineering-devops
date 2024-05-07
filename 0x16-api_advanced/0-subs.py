#!/usr/bin/python3
"""The number_of_subscribers."""

import requests


def number_of_subscribers(subreddit):
    """number of subscribers for a given sub-reddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    pathname = 'http://www.reddit.com/r/{}/about.json'
    agt = '0x16-api_advanced:project: v1.0.0 (by /u/firdaus_cartoon_jr)'
    r = requests.get(pathname.format(subreddit),
        headers={'User-Agent': agt}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
