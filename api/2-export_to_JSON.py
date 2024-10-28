#!/usr/bin/python3
"""
Module to fetch user information and export TODO list to a JSON file
"""
import json
import requests
import sys


def get_employee_info(employee_id):
    """
    Get employee information by employee ID
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    return response.json()


def get_employee_todos(employee_id):
    """
    Get the TODO list of the employee by employee ID
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    return response.json()


def export_to_json(employee_id, todos):
    """
    Export TODO list to a JSON file
    """
    filename = f"{employee_id}.json"
    with open(filename, "w") as file:
        json.dump({employee_id: todos}, file)


def main(employee_id):
    """
    Main function to fetch user info and TODO list, then export to JSON
    """
    user_info = get_employee_info(employee_id)
    todos_info = get_employee_todos(employee_id)

    employee_username = user_info["username"]

    todos_info_sorted = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_username
        } for task in todos_info
    ]

    export_to_json(employee_id, todos_info_sorted)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
