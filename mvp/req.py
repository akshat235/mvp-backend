import requests
import json



api_url = 'http://127.0.0.1:5000/auth/register' 
user_data = {
    "username": 'akshat@gmail.com', "password": 'Akshat@1234', "firstName": 'Akshat',
      "lastName": 'Gupta', "dob": '1000-10-10'}

response = requests.post(api_url, json=user_data)
if response.status_code == 201:
    print("User registered successfully.")
else:
    print("Failed to register the user. Status code:", response.status_code)
    print("Response:", response.text)


# login_url = "http://127.0.0.1:5000/auth/login"  
# credentials = {
#     "username": "Aksha@g.com",
#     "password": "Akshat@1234"
# }
# response = requests.post(login_url, json=credentials)
# if response.status_code == 200:
#     print("Login successful")
# elif response.status_code == 401:
#     print("Login failed. Check your credentials")
# else:
#     print("An error occurred")
