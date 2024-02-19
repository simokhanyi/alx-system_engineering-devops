#!/usr/bin/python3
"""Exports data in the CSV format"""


if __name__ == "__main__":
    import csv
    import requests
    import sys

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    # Fetching user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to fetch user data for employee ID {employee_id}")
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get('name')  # Using .get() method

    # Fetching todos
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch TODO list for employee ID {employee_id}")
        sys.exit(1)

    todos_data = todos_response.json()

    # Writing to CSV file
    csv_file_name = f"{employee_id}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                         "TASK_TITLE"])

        for todo in todos_data:
            task_completed_status = (
                "True" if todo.get('completed') else "False"
            )
            writer.writerow([employee_id, employee_name, task_completed_status,
                             todo.get('title')])
