
#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predictflask'

customer = {"job": "retired", "duration": 445, "poutcome": "success"}

response = requests.post(url, json=customer).json()
print(response)
