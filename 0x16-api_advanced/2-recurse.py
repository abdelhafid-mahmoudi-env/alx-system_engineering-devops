#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-Agent": "reddit-{}".format(subreddit)}
    params = {"after": after} if after else None

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        if data and data.get("children"):
            for post in data.get("children"):
                hot_list.append(post.get("data").get("title"))
            after = data.get("after")
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
    return None
