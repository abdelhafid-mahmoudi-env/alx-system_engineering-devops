#!/usr/bin/python3
"""
100-count
"""
import requests


def count_words(subreddit, word_list, after=None, word_counts={}):
    """
    Recursive function to count occurrences of keywords in hot articles of a subreddit
    """
    if not word_list:
        # Base case: when there are no more keywords to count
        sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
        return

    word = word_list.pop(0).lower()  # Get and remove the first word from the list
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-Agent": "reddit-{}".format(subreddit)}
    params = {"after": after} if after else None

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        if data and data.get("children"):
            for post in data.get("children"):
                title = post.get("data").get("title").lower()
                word_counts[word] = word_counts.get(word, 0) + title.count(word)
            after = data.get("after")
            if after:
                return count_words(subreddit, word_list, after, word_counts)
            else:
                return count_words(subreddit, word_list, None, word_counts)

    # No matches or subreddit is invalid
    if word_list:
        count_words(subreddit, word_list, None, word_counts)
    else:
        sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
