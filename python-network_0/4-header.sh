#!/bin/bash
# Sends a GET request to the URL with a custom header X-School-User-Id: 98
curl -s -H "X-School-User-Id: 98" "$1"
