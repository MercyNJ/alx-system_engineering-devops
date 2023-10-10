#!/usr/bin/python3
"""
Returns no of subscribers for given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API,returns no of subscribers
    for given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': 'MyRedditBot/1.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = requests.get(url, headers=user_agent)

        if response.status_code == 200:
            results = response.json()
            return results.get('data').get('subscribers')
        elif response.status_code == 404:
            return 0
        else:
            print('Error: {}'.format(response.status_code))
            return 0

    except requests.exceptions.RequestException as e:
        print('RequestException: {}'.format(e))
        return 0
