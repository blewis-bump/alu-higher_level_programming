#!/bin/bash
curl -s -X OPTIONS "$1" -v 2>&1 | grep "Allow:"
