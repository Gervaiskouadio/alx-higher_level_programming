#!/bin/bash
# A Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
url -sX GET $1 -H "X-School-User-Id: 98" -L
