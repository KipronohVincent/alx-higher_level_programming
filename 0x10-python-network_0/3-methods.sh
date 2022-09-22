#!/bin/bash
# Bash script that takes in URL and display all HTTP methods
curl -sI "$1" | grep "Allow: " | cut -d' ' -f 2-
