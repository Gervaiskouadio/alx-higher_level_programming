#!/bin/bash

# A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the reonse

curl -sX GET $1 -L
