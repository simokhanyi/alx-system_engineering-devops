#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""


import requests
import sys


def fetch_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    # Fetching user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to fetch user data for employee ID {employee_id}")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetching todos
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch TODO list for employee ID {employee_id}")
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_count = sum(task['completed'] for task in todos_data)

    # Displaying progress
    if employee_name:
        print(f"Employee {employee_name} is done with tasks"
              f"({completed_count}/{total_tasks}):")
        for task in todos_data:
            if task['completed']:
                print(f"\t{task['title']}")
    else:
        print(f"Employee with ID {employee_id} not found")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
