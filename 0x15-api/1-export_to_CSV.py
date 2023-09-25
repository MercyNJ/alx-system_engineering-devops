#!/usr/bin/python3
"""
A script making a GET request to a REST API.
Displays an employess's todo list's progress.
"""

import requests
import sys

if __name__ == '__main__':
    empl_id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    empl_url = baseUrl + "/" + empl_id
    response = requests.get(empl_url)
    empl_username = response.json().get('username')

    todoUrl = empl_url + "/todos"
    response = requests.get(todoUrl)

    tasks = response.json()

    with open('{}.csv'.format(empl_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'.format(
                empl_id, empl_username, task.get(
                    'completed'), task.get('title')))
