#!/bin/bash
# This script sends a POST request and displays the body response
curl -sd "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"
