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
    empl_name = response.json().get('name')

    todoUrl = empl_url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    count_complete = 0
    complete_tasks = []

    for task in tasks:
        if task.get('completed'):
            complete_tasks.append(task)
            count_complete += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(empl_name, count_complete, len(tasks)))

    for task in complete_tasks:
        print("\t {}".format(task.get('title')))
