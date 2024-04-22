#!/usr/bin/python3
'''A script that gathers employee name completed
tasks and total number of tasks from an API
'''

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employee_id = int(sys.argv[1])
            emp_req = requests.get(f'{REST_API}/users/{employee_id}').json()
            task_req = requests.get(f'{REST_API}/todos').json()
            emp_name = emp_req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == employee_id, task_req))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                f'Employee {emp_name} is done with tasks({len(completed_tasks)}/{len(tasks)}):'
            )
            for task in completed_tasks:
                print(f'\t{task.get("title")}')
