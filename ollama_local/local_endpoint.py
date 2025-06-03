import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "gemma3:4b",
    "prompt": "Hi can you explain what LBW is?",
    "stream": False
}

response = requests.post(url, json=data)

if response.ok:
    print(response.json()["response"])
else:
    print("error: ", response.status_code, response.text)