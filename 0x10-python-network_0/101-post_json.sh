#!/bin/bash
# This script sends a JSON POST request
curl -s "$1" -X POST -H "Content-Type: application/json" -d "$2"
