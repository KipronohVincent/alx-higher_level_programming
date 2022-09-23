#!/usr/bin/python3
"""
script que haga un fetch a https://intranet.hbtn.io/status con request
"""
if __name__ == "__main__":
    import requests

    url = "https://intranet.hbtn.io/status"
    data_req = requests.get(url)

    print("Body response:")
    print("\t- type:", type(data_req.text))
    print("\t- content:", data_req.text)
