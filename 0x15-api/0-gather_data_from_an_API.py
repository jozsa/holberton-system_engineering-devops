#!/usr/bin/python3
"""
Returns information about an employee
whose ID is passed into the script.
"""


import requests
import sys

# URL to make API requests from
url = 'https://jsonplaceholder.typicode.com'

# Employee information
employee = requests.get('{}/users/{}'.format(url, sys.argv[1]))
employee_name = employee.json().get('name')

# Todo list information
tasks = requests.get('{}/todos?userId={}'.format(url, sys.argv[1]))
task_list = tasks.json()
total_tasks = len(task_list)
completed_tasks = sum(1 for task in task_list if task.get('completed'))

# Printing employee name, number of tasks, and each task
print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                      completed_tasks,
                                                      total_tasks))
for task in task_list:
    if task.get('completed'):
        print(' \t{}'.format(task.get('title')))
