#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/user"
    user = sys.argv[1]
    passwd = sys.argv[2]
    data_res = requests.get(url, auth=(user, passwd))

    try:
        data_json = data_res.json()
        print(data_json["id"])
    except Exception:
        print("None")
