#!/bin/bash
# Bash script that sends a request to a URL passed as an argument
curl -sI -w '%{response_code}' "$1" -o /dev/null
