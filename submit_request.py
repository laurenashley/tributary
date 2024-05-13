import requests
import json

BASE_URL = "http://0.0.0.0:8000"

# test /record endpoint
def test_record_endpoint(engine_temperature):
  payload = {"engine_temperature": engine_temperature}
  headers = {"Content-Type": "application/json"}
  response = requests.post(BASE_URL + "/record", data=json.dumps(payload), headers=headers)
  print("Response from /record endpoint:", response.text)

def test_collect_endpoint():
  response = requests.post(BASE_URL + "/collect")
  print("Response from /collect endpoint:", response.text)

test_record_endpoint(20)

test_collect_endpoint()