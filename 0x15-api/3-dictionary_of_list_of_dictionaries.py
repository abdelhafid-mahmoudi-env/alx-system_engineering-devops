#!/usr/bin/python3
"""Script to export todos of all employees in JSON format"""
import json
import requests

if __name__ == "__main__":
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Retrieve user data
    users_data = requests.get(base_url + "users").json()

    # Dictionary to store todos of all employees
    all_todos = {}

    # Iterate over each user
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")

        # Retrieve todos for the user
        todos_url = base_url + "todos"
        todos_params = {"userId": user_id}
        todos_response = requests.get(todos_url, params=todos_params)
        todos_data = todos_response.json()

        # List to store todos of the current user
        user_todos = []

        # Iterate over each todo of the user
        for todo in todos_data:
            todo_title = todo.get("title")
            completed = todo.get("completed")

            # Add todo details to the list
            user_todos.append({
                "task": todo_title,
                "completed": completed,
                "username": username
            })

        # Add user's todos to the dictionary
        all_todos[user_id] = user_todos

    # Write data to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_todos, json_file)
