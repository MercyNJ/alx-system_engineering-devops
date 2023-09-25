#!/usr/bin/python3
"""
A script making a GET request to a REST API.
Displays an employess's todo list's progress.
"""
import json
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

    data = {empl_id: []}
    for task in tasks:
        data[empl_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": empl_username
        })
    with open('{}.json'.format(empl_id), 'w') as fl:
        json.dump(data, fl)
