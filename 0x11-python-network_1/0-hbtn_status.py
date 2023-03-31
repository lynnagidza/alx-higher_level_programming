"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
# !/usr/bin/python3
# Module with code that fetches a URL
import urllib.request


if __name__ == "__main__":
    # fetches a URL
    URL = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(URL) as response:
        html = response.read()
    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {html.decode}")
