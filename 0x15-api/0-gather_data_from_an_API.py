#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Fetches and prints information about an employee's TODO list progress.

    Args:
        employee_id (str): The ID of the employee to fetch.

    Raises:
        ValueError: If the provided employee ID is not a positive integer.
        Exception: If there's an issue fetching data from the API.
    """
    if not employee_id.isdigit() or int(employee_id) <= 0:
        raise ValueError("Employee ID must be a positive integer.")

    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(employee_id))
    todos_response = requests.get(
            url + "todos",
            params={"userId": employee_id}
    )

    # Check if both requests were successful
    if user_response.status_code != 200 or todos_response.status_code != 200:
        raise Exception("Error: Unable to fetch data from the API.")

    user = user_response.json()
    todos = todos_response.json()

    completed_tasks = [
            todo.get("title") for todo in todos
            if todo.get("completed")
    ]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))

    for task in completed_tasks:
        print("\t{}".format(task))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        fetch_employee_todo_progress(employee_id)
    except ValueError as ve:
        print("Error:", ve)
        sys.exit(1)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
