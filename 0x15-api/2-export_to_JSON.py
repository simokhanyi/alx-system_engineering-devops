#!/usr/bin/python3
"""
script to export data in the JSON format and records
all tasks that are owned by this employee
"""

import sys
import requests
import json


def fetch_employee_todo_progress(employee_id):
    """
    Fetches employee's TODO list from a REST API and exports it to a JSON file.

    Args:
    - employee_id (int): The ID of the employee.

    Returns:
    - None

    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    # Fetching user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to fetch user data for employee ID {employee_id}")
        return

    user_data = user_response.json()
    username = user_data.get('username')

    # Fetching todos
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch TODO list for employee ID {employee_id}")
        return

    todos_data = todos_response.json()

    # Constructing JSON data
    json_data = {str(employee_id): []}
    for todo in todos_data:
        json_data[str(employee_id)].append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        })

    # Writing to JSON file
    json_file_name = f"{employee_id}.json"
    with open(json_file_name, mode='w') as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
