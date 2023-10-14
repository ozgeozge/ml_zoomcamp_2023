
#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predictflask'

client = {"job": "unknown", "duration": 270, "poutcome": "failure"}

response = requests.post(url, json=client).json()
print(response)
