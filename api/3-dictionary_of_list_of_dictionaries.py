#!/usr/bin/python3
"""
Python script that exports data in the JSON format
"""
import json
import requests


def get_all_users():
    """
    Get the list of all users
    """
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()


def get_user_todos(user_id):
    """
    Get the TODO list for a given user ID
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": user_id})
    return response.json()


def export_all_todos_to_json(users):
    """
    Export all users' TODO lists to a JSON file
    """
    data = {
        user["id"]: [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
            } for todo in get_user_todos(user["id"])
        ] for user in users
    }
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)


def main():
    """
    Main function to fetch users and their TODO lists, then export to JSON
    """
    users = get_all_users()
    export_all_todos_to_json(users)

if __name__ == "__main__":
    main()
