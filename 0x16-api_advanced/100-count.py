#!/usr/bin/python3
"""
parses the title of all hot articles, and prints
a sorted count of given keywords.
"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    Queries rEDDIT api, returns list of hot articles
    for a given subreddit.
    """

    global after
    user_agent = {'User-Agent': 'MyRedditBot/1.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    query_params = {'after': after}
    results = requests.get(url, params=query_params, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        next_page_data = results.json().get("data").get("after")
        if next_page_data is not None:
            after = next_page_data
            recurse(subreddit, hot_list)
        current_titles = results.json().get("data").get("children")
        for title_ in current_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)


def count_words(subreddit, word_list, word_counts=None):
    """Achieves the sorting"""
    if word_counts is None:
        word_counts = {}
    hot_articles = recurse(subreddit)
    if hot_articles is None:
        return
    for article_title in hot_articles:
        words = article_title.lower().split()
        words = [word.strip('.,!') for word in words]

        for word in words:
            if word.lower() in [w.lower() for w in word_list]:
                if word.lower() in word_counts:
                    word_counts[word.lower()] += 1
                else:
                    word_counts[word.lower()] = 1
    sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print("{}: {}".format(word, count))
