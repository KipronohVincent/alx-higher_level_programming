#!/bin/bash
#Bash script that takes in a URL, sends a POST request to the passed URL
curl -sX POST "$1" --data "email=test@gmail.com" --data "subject=I will always be here for PLD"

