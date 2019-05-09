#!/usr/bin/python3
"""
This module has one function: number_of_subscribers(subreddit).
"""
import requests
import sys


def top_ten(subreddit):
    # URL and headers to make API requests from
    url = 'https://reddit.com/r'

    # Subscriber count information
    top_ten = requests.get('{}/{}/top/.json?count=10'
                           .format(url, subreddit),
                           headers={'User-Agent': 'Mozilla/5.0'})\
        .json().get('data').get('children')[:10]

    if not top_ten:
        top_ten = None

    for value in top_ten:
        print(value.get('data').get('title'))
