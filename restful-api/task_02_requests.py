#!/usr/bin/python3

"""
modulo documentado task 02
"""


import requests
import csv


def fetch_and_print_posts():
    """
    function documented task 02
    """
    request = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {request.status_code}")

    if request.status_code == 200:
        posts = request.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    request = requests.get("https://jsonplaceholder.typicode.com/posts")

    if request.status_code == 200:
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows([
                {
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                }
                for post in request.json()
                ])
    else:
        print("Failed to fetch posts")
