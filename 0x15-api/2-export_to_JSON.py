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

    data = {
            empl_id: [
                {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": empl_username
                }
                for task in tasks
                ]
            }
    json_filename = "{}.json".format(empl_id)
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file)
