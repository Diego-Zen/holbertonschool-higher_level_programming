#!/bin/bash
# This script sends a request and displays only the status code response
curl -s -o /dev/null -w "%{http_code}" "$1"
