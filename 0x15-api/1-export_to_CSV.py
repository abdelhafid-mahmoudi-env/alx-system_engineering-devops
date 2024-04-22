#!/usr/bin/python3
""" Script to export data into a CSV format """
import csv
import requests
import sys

if __name__ == "__main__":
    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Extract user ID from command line argument
    uid = sys.argv[1]

    # Retrieve user data
    u_resp = requests.get(url + "users/{}".format(uid))
    u_data = u_resp.json()
    uname = u_data.get("username")

    # Retrieve todo data for the user
    t_resp = requests.get(url + "todos", params={"userId": uid})
    t_data = t_resp.json()

    # Write data to a CSV file
    with open("{}.csv".format(uid), "w", newline="") as c_file:
        c_writer = csv.writer(c_file, quoting=csv.QUOTE_ALL)
        for task in t_data:
            c_writer.writerow([
                uid,
                uname,
                task.get("completed"),
                task.get("title")
            ])
