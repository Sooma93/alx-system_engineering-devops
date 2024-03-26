#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)
    user_data = response.json()
    name = user_data.get('name')

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
    response = requests.get(url)
    todos_data = response.json()

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    total_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(name, total_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
