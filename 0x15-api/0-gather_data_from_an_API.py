#!/usr/bin/python3
"""
Script that retrieves information about an employee's TODO list progress
using a REST API.
"""

import sys
import requests


def fetch_employee_todo_progress(employee_id):
    """
    Retrieves and prints information about an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee to fetch TODO list progress for.
    """
    url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': employee_id}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error: Unable to fetch data")
        return

    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    employee_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                                 .format(employee_id)).json()['name']

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_completed_tasks, total_tasks))

    for task in completed_tasks:
        print("\t{}".format(task['title']))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
