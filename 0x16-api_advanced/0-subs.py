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
    for a given subreddit using the provided access token.
    """
    # Define custom User-Agent headers
    u_agent = (
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Ubuntu Chromium/96.0.4664.110 '
        'Chrome/96.0.4664.110 Safari/537.36'
    )

    headers = {
        'User-Agent': u_agent,
        'Content-Type': 'application/x-json',
        'Accept': 'application/x-json'
    }

    # Construct URL for the API endpoint
    url = f"https://api.reddit.com/r/{subreddit}/about.json?keyphrase=witcher"
    res = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if res.status_code != 200:
        return 0

    # Parse the JSON response
    dic = res.json()

    # Check if the 'data' key exists in the response
    if 'data' not in dic:
        return 0

    # Check if the 'subscribers' key exists in the 'data' dictionary
    if 'subscribers' not in dic.get('data'):
        return 0

    # Return the number of subscribers
    return res.json()['data']['subscribers']
