
import requests
curl = "http://127.0.0.1:5000/dashboard/get_test_responses"

response = requests.get(curl)
if response.status_code == 200:
  print("Success")
  questions = response.json()
  print(questions)
#   print(questions)
else:
  print("Error", response.json())

# Test 404 error
response = requests.get(curl) 
if response.status_code == 404:
  print("Not found error", response.json())

# Test 500 error 
# Stop MongoDB server to trigger error
response = requests.get(curl)
if response.status_code == 500:
  print("Server error", response.text)