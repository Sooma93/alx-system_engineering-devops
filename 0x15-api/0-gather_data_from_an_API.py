#!/usr/bin/python3
"""
Queries external API for user todo task information
"""
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]

    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params={'id': user_id})
    response = requests.get('https://jsonplaceholder.typicode.com/todos',
                            params={'userId': user_id})

    tasks = response.json()
    employee = user.json()[0].get('name')

    total = 0
    completed = 0
    task_list = []

    for task in tasks:
        if task.get('completed'):
            completed += 1
            task_list.append(task.get('title'))
        total += 1

    print("Employee {} is done with tasks({}/{}):".
          format(employee, completed, total))
    for task in task_list:
        print("\t {}".format(task))
