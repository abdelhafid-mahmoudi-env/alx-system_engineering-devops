#!/usr/bin/python3
"""
100-count
"""
import requests


def count_words(subreddit, word_list, after=None, word_counts={}):
    """
    Recursive function to count occurrences.
    """
    if not word_list:
        sorted_counts = sorted(
                word_counts.items(),
                key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
        return

    word = word_list.pop(0).lower()
    pathname = "https://www.reddit.com/r/{}/hot.json?limit=100"
    url = pathname.format(subreddit)
    headers = {"User-Agent": "reddit-{}".format(subreddit)}
    params = {"after": after} if after else None

    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json().get("data")
        if data and data.get("children"):
            for post in data.get("children"):
                title = post.get("data").get("title").lower()
                wrding = word_counts.get(word, 0)
                titling = title.count(word)
                word_counts[word] = wrding + titling
            after = data.get("after")
            if after:
                return count_words(subreddit, word_list, after, word_counts)
            else:
                return count_words(subreddit, word_list, None, word_counts)

    if word_list:
        count_words(subreddit, word_list, None, word_counts)
    else:
        sorted_counts = sorted(
                word_counts.items(),
                key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
