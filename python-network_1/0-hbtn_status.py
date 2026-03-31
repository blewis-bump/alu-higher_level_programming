#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using urllib."""
import urllib.request
import ssl


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    with urllib.request.urlopen(url, context=ctx) as response:
        body = response.read()
    print("Body response:")
    print("	- type: {}".format(type(body)))
    print("	- content: {}".format(body))
    print("	- utf8 content: {}".format(body.decode("utf-8")))
