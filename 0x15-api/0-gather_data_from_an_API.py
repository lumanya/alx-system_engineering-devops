#!/usr/bin/python3
"""
 Python script, using REST API, for a given employee ID, List about his/her
 to do list progress. https://jsonplaceholder.typicode.com/
"""
import requests
from sys import argv


if __name__ == "__main__":
    """ request user name from API"""
    employeeId = int(argv[1])
    done = 0
    tasks = 0
    task_title = {}

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    r = requests.get(user_url)
    employee = r.json().get('name')

    # Gettig todos list
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    r_todo = requests.get(todo_url)
    for todo in r_todo.json():
        if todo.get('userId') == employeeId:
            tasks += 1
            if todo.get('completed'):
                done += 1

    print(f"Employee {employee} is done with tasks({done}/{tasks})")
    for todo in r_todo.json():
        if todo.get('userId') == employeeId and todo.get('completed'):
            print("\t {}".format(todo.get('title')))
