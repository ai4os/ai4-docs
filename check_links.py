"""
Parse all URLs of the documentation and check that they work
"""

import os
import re
import requests
from rich import print as print
import urllib3


# Disable warning from python-nomad
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


session = requests.Session()

source_folder = 'source'

links = []
for root, _, files in os.walk(source_folder):
    for file in files:
        if file.endswith('.rst'):
            print(f"[blue]Parsing: {file}[/blue]")
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                content = file.read()
                links += re.findall(r'<\s*(http[s]?://[^>\s]+)\s*>`__', content)

# Remove duplicates
links = set(links)
links = sorted(links)

# Check links
for link in links:
    try:
        # We use GET and not HEAD, because HEAD does not return the correct status codes
        r = session.get(link, allow_redirects=True, timeout=5, verify=False)
        if r.ok:
            print(f"[grey]{link}[/grey]")
        elif r.status_code == 404:
            print(f"[orange1]{link}, {r.status_code}[/orange1]")
        else:
            print(f"[magenta3]{link}, {r.status_code}[/magenta3]")

    except requests.RequestException:
            print(f"[red]{link}, invalid URL[/red]")
