#!/usr/bin/python3
"""
Module to fetch user information and export TODO list to a CSV file
"""
import csv
import requests
from sys import argv


def get_employee_info(employee_id):
    """
    Get employee information by employee ID
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    return response.json()


def get_employee_todos(employee_id):
    """
    Get the TODO list of the employee by employee ID
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(url)
    return response.json()


def export_to_csv(employee_id, username, todos):
    """
    Export TODO list to a CSV file
    """
    filename = f'{employee_id}.csv'
    with open(filename, mode='w') as file:
        file_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for todo in todos:
            rowData = [employee_id, username, todo['completed'], todo['title']]
            file_writer.writerow(rowData)


def main(employee_id):
    """
    Main function to fetch user info and TODO list, then export to CSV
    """
    user = get_employee_info(employee_id)
    username = user.get("username")

    todos = get_employee_todos(employee_id)

    export_to_csv(employee_id, username, todos)


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
