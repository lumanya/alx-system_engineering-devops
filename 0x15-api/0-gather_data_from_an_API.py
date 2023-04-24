#!/usr/bin/python3
"""
 Python script, using REST API, for a given employee ID, List about his/her
 to do list progress. https://jsonplaceholder.typicode.com/
"""
from sys import argv
import requests


if __name__ == "__main__":
    """ request user name from API"""
    task_done = 0
    total_task = 0
    task_title = {}

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    r = requests.get(user_url)
    user_data = r.json()

    # Gettig todos list
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    r_todo = requests.get(todo_url)
    for todo in r_todo.json():
        if todo.get('userId') == int(argv[1]):
            total_task += 1
            if todo.get('completed') == True:
                task_done += 1

    print("Employee {} is done with tasks({}/{})".\
          format(user_data.get('name'), task_done, total_task))
    for todo in r_todo.json():
        if todo.get('userId') == int(argv[1]) and todo.get('completed') == True:
            print("\t {}".format(todo.get('title')))
