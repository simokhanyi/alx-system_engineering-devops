#!/usr/bin/python3
"""Exports data in the CSV format"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    user_id = sys.argv[1]

    # Fetch user data
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}")
    user_data = user_response.json()
    user_name = user_data.get('username')

    # Fetch todos data
    todos_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos")
    todos_data = todos_response.json()

    # Write to CSV file
    filename = f"{user_id}.csv"
    with open(filename, mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos_data:
            if task.get('userId') == int(user_id):
                writer.writerow([user_id, user_name,
                                 str(task.get('completed')),
                                 task.get('title')])
