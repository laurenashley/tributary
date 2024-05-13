import requests

payload = {"engine_temperature": 0.3}

# Send POST request to the server
response = requests.post("http://0.0.0.0:8000/record", json=payload)

print(response.content)