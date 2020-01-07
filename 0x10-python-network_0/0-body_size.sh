#!/bin/bash
# This script prints the content length of a request
curl -sI "$1" | grep -i content-length | awk '{print $2}'
