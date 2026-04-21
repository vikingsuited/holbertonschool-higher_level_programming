#!/usr/bin/python3
"""
Consuming and processing data from an API using Python
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetches all posts and saves them into a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        structured_data = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']}
            for p in posts
        ]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_data)
