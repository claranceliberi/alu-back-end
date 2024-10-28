#!/usr/bin/python3
"""
Script that retrieves TODO list progress for a given employee ID from a REST API.

This module queries a JSON placeholder API to get employee and TODO information,
processes it, and displays task completion progress in a specified format.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve and display TODO list progress for a specific employee.

    Args:
        employee_id (int): The ID of the employee to query

    Returns:
        None: Prints formatted output to stdout
    """
    # API base URL
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    employee_url = f"{base_url}/users/{employee_id}"
    try:
        employee_response = requests.get(employee_url)
        employee_response.raise_for_status()
        employee = employee_response.json()
    except requests.RequestException as e:
        print(f"Error fetching employee data: {e}")
        sys.exit(1)

    # Get TODO list for employee
    todos_url = f"{base_url}/todos?userId={employee_id}"
    try:
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos = todos_response.json()
    except requests.RequestException as e:
        print(f"Error fetching TODO data: {e}")
        sys.exit(1)

    # Calculate progress
    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo.get('completed'))
    employee_name = employee.get('name')

    # Display progress
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")

    # Display completed tasks
    for todo in todos:
        if todo.get('completed'):
            print(f"\t {todo.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
