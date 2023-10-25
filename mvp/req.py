import requests
import json



# api_url = 'http://127.0.0.1:5000/auth/register' 
# user_data = {
#     "username": 'akshat@gmail.com', "password": 'Akshat@1234', "firstName": 'Akshat',
#       "lastName": 'Gupta', "dob": '1000-10-10'}

# response = requests.post(api_url, json=user_data)
# if response.status_code == 201:
#     print("User registered successfully.")
# else:
#     print("Failed to register the user. Status code:", response.status_code)
#     print("Response:", response.text)


login_url = "http://127.0.0.1:5000/auth/login"  
credentials = {
    "username": "akshat@gmail.com",
    "password": "Akshat@1234"
}
response = requests.post(login_url, json=credentials)
print(response.json())
if response.status_code == 200:
    print("Login successful")
elif response.status_code == 401:
    print("Login failed. Check your credentials")
else:
    print("An error occurred")



# Replace this URL with the actual URL of your Flask app
# qurl = "http://127.0.0.1:5000/test/questions"

# try:
#     response = requests.get(qurl)

#     if response.status_code == 200:
#         questions = response.json()
#         for question in questions:
#             if 'id' in question and 'question_body' in question and 'options' in question:
#                 print(f"Question ID: {question['id']}")
#                 print(f"Question Body: {question['question_body']}")
#                 print(f"Options: {question['options']}")
#                 print("-------------------")
#             else:
#                 print("Invalid question structure in the response.")
#     else:
#         print(f"Failed to retrieve questions. Status code: {response.status_code}")
# except requests.exceptions.RequestException as e:
#     print(f"Error: {e}")
