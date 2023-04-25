#!/usr/bin/python3
"""
 Python script, using REST API, for a given employee ID, List about his/her
 to do list progress. https://jsonplaceholder.typicode.com/
"""

import requests
import sys


def display():
    """ return API data"""
    user_id = int(sys.argv[1])
    user = requests.get(f"http://jsonplaceholder.typicode.com/users/{user_id}")
    EMPLOYEE_NAME = user.json().get('name')
    TOTAL_NUM_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        if todo.get('userId') == user_id:
            TOTAL_NUM_OF_TASKS += 1
            if todo.get('completed'):
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(todo.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUM_OF_TASKS))

    for task in TASK_TITLE:
        print("\t {}".format(task))


if __name__ == "__main__":
    display()
