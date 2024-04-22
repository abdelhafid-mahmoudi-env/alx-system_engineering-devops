#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys


def export_todo_list(user_id):
    """
    Exports to-do list information for a given employee ID to CSV format.

    Args:
        user_id (str): The ID of the user whose to-do list is to be exported.

    Returns:
        None
    """
    url = "https://jsonplaceholder.typicode.com/"

    # Fetching user data and to-dos
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Writing to CSV
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # Writing CSV header
        header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer.writerow(header)
        # Writing to CSV row by row
        for todo in todos:
            row_data = [
                user_id,
                username,
                todo.get("completed"),
                todo.get("title")
            ]
            writer.writerow(row_data)


if __name__ == "__main__":
    # Fetching user ID from command line arguments
    user_id = sys.argv[1]
    export_todo_list(user_id)
