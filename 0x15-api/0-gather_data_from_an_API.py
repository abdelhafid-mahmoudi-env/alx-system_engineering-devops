#!/usr/bin/python3
"""Retrieves to-do list information for a given employee ID."""

import requests
import sys

if __name__ == "__main__":
    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user information based on provided employee ID
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    
    # Fetch to-do list for the specified employee ID
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # Filter completed tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    
    # Print the employee's progress
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    
    # Print titles of completed tasks
    [print("\t {}".format(c)) for c in completed]
