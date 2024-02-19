#!/usr/bin/python3
"""
script to export data in the JSON format and records
all tasks from all employees
"""

import requests
import json


def fetch_all_employee_todo_progress():
    """
    Fetches all employees' TODO lists from a REST API and exports
    them to a JSON file.

    Args:
    - None

    Returns:
    - None

    """
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'

    # Fetching users
    users_response = requests.get(users_url)
    if users_response.status_code != 200:
        print("Failed to fetch users data")
        return

    users_data = users_response.json()

    # Constructing JSON data
    json_data = {}
    for user in users_data:
        user_id = str(user['id'])
        username = user.get('username')
        todos_url = f'{base_url}/todos?userId={user_id}'
        todos_response = requests.get(todos_url)
        if todos_response.status_code == 200:
            todos_data = todos_response.json()
            json_data[user_id] = []
            for todo in todos_data:
                json_data[user_id].append({
                    "username": username,
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                })

    # Writing to JSON file
    json_file_name = "todo_all_employees.json"
    with open(json_file_name, mode='w') as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == "__main__":
    fetch_all_employee_todo_progress()
