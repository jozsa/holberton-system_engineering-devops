#!/usr/bin/python3
"""
Returns information about an employee
whose ID is passed into the script.

Exports data in JSON format
"""


import json
import requests
import sys

# URL to make API requests from
url = 'https://jsonplaceholder.typicode.com'

# User ID to request
user_id = sys.argv[1]

# Employee information
employee = requests.get('{}/users/{}'.format(url, user_id))
username = employee.json().get('username')

# Todo list information
tasks = requests.get('{}/todos?userId={}'.format(url, user_id))
task_list = tasks.json()

# JSON formatted data to insert into JSON file
json_dict = {user_id: [{"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": username}
                       for task in task_list]}

# Export json data into json file
with open('{}.json'.format(user_id), 'w') as fp:
    json.dump(json_dict, fp)
