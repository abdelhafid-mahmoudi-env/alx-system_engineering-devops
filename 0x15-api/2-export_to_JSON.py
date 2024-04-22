#!/usr/bin/python3
""" Script to export data in JSON format """
import json
import requests
import sys

if __name__ == "__main__":
    # Check if user ID is provided
    if len(sys.argv) < 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    # Extract user ID from command line argument
    uid = sys.argv[1]

    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve user data
    u_data = requests.get(url + "users/{}".format(uid)).json()
    uname = u_data.get("username")

    # Retrieve todo data for the user
    t_data = requests.get(url + "todos", params={"userId": uid}).json()

    # Write data to a JSON file
    with open("{}.json".format(uid), "w") as f:
        json.dump({uid: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": uname
            } for task in t_data]}, f)
