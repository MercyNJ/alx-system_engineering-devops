#!/usr/bin/python3
"""
Returns a list containing the titles of all hot articles
for a given subreddit.
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
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        current_titles = results.json().get("data").get("children")
        for title_ in current_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
