#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "reddit-{}".format(subreddit)}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        if data and data.get("children"):
            for post in data.get("children"):
                print(post.get("data").get("title"))
        else:
            print("None")
    else:
        print("None")
