#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    m = requests.get(url)
    print(m.headers.get("X-Request-Id"))
