#!/usr/bin/python3
"""
script that returns information about his/her TODO list progress
for a given employee ID
"""

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Fetches employee TODO list progress from a REST API and displays it.

    Args:
    - employee_id (int): The ID of employee whose progress needs to be fetched.

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
    employee_name = user_data.get('name')  # Using .get() method

    # Fetching todos
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch TODO list for employee ID {employee_id}")
        return

    todos_data = todos_response.json()

    # Counting completed tasks
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    total_tasks = len(todos_data)
    completed_count = len(completed_tasks)

    # Displaying progress
    if employee_name:  # Check if employee_name is not None
        print(
            "Employee {} is done with tasks ({}/{})".format(
                employee_name, completed_count, total_tasks
            )
        )
        for task in completed_tasks:
            print(f"\t{task['title']}")
    else:
        print(f"Employee with ID {employee_id} not found")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
