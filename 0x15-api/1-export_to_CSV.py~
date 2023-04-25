#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees and write to scv"""

import csv
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        task.pop('id', None)
        task.update({'user_name': employeeName})

    filename = "{}.csv".format(employeeId)
    with open(filename, 'w') as file:
        # Difine fields name
        fieldnames = ['userId', 'user_name', 'completed', 'title']
        writer = csv.DictWriter(file, fieldnames=fieldnames, 
                                quoting=csv.QUOTE_ALL)

        # Write the data to the file
        for row in tasks:
            writer.writerow(row)
