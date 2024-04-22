#!/usr/bin/python3
"""
Gather data from an API and export to CSV
"""
import requests
import csv
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user_id
    response_user = requests.get(url_user)
    user_data = response_user.json()

    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId=' + user_id
    response_todos = requests.get(url_todos)
    todos_data = response_todos.json()

    filename = user_id + ".csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
        ])
        for task in todos_data:
            writer.writerow([
                user_id,
                user_data['username'],
                task['completed'],
                task['title']
            ])
