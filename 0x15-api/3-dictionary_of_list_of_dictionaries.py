#!/usr/bin/python3
"""
A script making a GET request to a REST API.
Displays an employess's todo list's progress.
"""

import json
import requests
import sys


if __name__ == '__main__':
    users_url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(users_url)
    users = response.json()

    data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        usr_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
                user_id)
        usr_url = usr_url + '/todos/'
        response = requests.get(usr_url)
        tasks = response.json()
        data[user_id] = []
        for task in tasks:
            data[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
