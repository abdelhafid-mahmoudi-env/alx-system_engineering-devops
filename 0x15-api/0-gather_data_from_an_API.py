#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/' + user_id
    response_user = requests.get(url)
    user_data = response_user.json()

    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + user_id
    response_todos = requests.get(url)
    todos_data = response_todos.json()

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]
    num_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        user_data['name'], num_completed_tasks, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task['title']))
