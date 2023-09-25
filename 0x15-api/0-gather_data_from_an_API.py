#!/usr/bin/python3
"""
A script making a GET request to a REST API.
Displays an employess's todo list's progress.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """ Display empl todo progress."""
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    try:
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employee_name = employee_data.get("name")
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        total_tasks = len(todos_data)
        completed_tasks = sum(
                1 for task in todos_data if task["completed"])
        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, completed_tasks, total_tasks))
        for task in todos_data:
            if task["completed"]:
                print("\t{}".format(task['title']))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
    except KeyError:
        print("Employee not found.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        get_employee_todo_progress(employee_id)
