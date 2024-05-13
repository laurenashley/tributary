import requests

url = "http://0.0.0.0:8000/record"
payload = {"engine_temperature": 0.3}

# Send POST request to the server
response = requests.post(url, json=payload)

if response.status_code == 200:
  print("Request successful")
  print("Response: ", response.text)
else:
  print("Request failed with status code:", response.status_code)