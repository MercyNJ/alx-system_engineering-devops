#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries Reddit API,prints titles of 1st
    10 hot posts in given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-Agent': 'MyRedditBot/1.0'}
    query_parameters = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    try:
        response = requests.get(
                url, headers=user_agent, params=query_parameters)
        results = response.json()

        obtained_data = results.get('data').get('children')
        for post in obtained_data:
            print(post.get('data').get('title'))

    except requests.exceptions.RequestException as e:
        print("RequestException: {}".format(e))
    except Exception:
        print("An error occurred")
