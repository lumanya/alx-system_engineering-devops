#!/usr/bin/python3
"""Accessing a REST API for to lists of employees and list"""

import json
import requests
import sys


if __name__ == '__main__':
    users_api = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(users_api)
    users = response.json()
    dictionary = {}

    for user in users:
        userId = user.get('id')
        url = f'https://jsonplaceholder.typicode.com/users/{userId}/todos'
        todos = requests.get(url).json()
        dictionary[userId] = []
        for task in todos:
            dictionary[userId].append({
                "username": user.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
                })

    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
