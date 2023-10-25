# a= [{'options': ['Mg + O2 → MgO', '2H2 + O2 → 2H2O', 'CaCO3 → CaO + CO2', 'NaCl → Na + Cl'], 'questionBody': 'Which of the following is an example of an oxidation reaction?', 'questionId': 1}, {'options': ['11', '13', '15', '17'], 'questionBody': 'If f(x) = 2x + 3, what is f(5)?', 'questionId': 2}, {'options': ['Tulsidas', 'Valmiki', 'Vyasa', 'Kalidasa'], 'questionBody': 'Who wrote the epic Ramayana?', 'questionId': 3}, {'options': ['Tiger', 'Lion', 'Elephant', 'Peacock'], 'questionBody': 'What is the national animal of India?', 'questionId': 4}, {'options': ['Nitrogen', 'Oxygen', 'Carbon dioxide', 'Argon'], 'questionBody': "Which of the following gases is most abundant in the earth's atmosphere?", 'questionId': 5}, {'options': ['Junko Tabei', 'Bachendri Pal', 'Santosh Yadav', 'Dickie Dolma'], 'questionBody': 'Who was the first woman to climb Mount Everest?', 'questionId': 6}, {'options': ['Australia', 'Antarctica', 'Europe', 'Africa'], 'questionBody': 'What is the smallest continent on Earth?', 'questionId': 7}, {'options': ['Rajasthan', 'Maharashtra', 'Madhya Pradesh', 'Gujarat'], 'questionBody': 'In which state is the Ajanta Cave situated?', 'questionId': 8}, {'options': ['Thomas Edison', 'Alexander Graham Bell', 
# 'Nikola Tesla', 'Guglielmo Marconi'], 'questionBody': 'Who invented the telephone?', 'questionId': 9}, {'options': ['Sydney', 'Melbourne', 'Canberra', 'Perth'], 'questionBody': 'What is the capital of Australia?', 'questionId': 10}, {'options': ['Mark Twain', 'Jules Verne', 'Herman Melville', 'Alexandre Dumas'], 'questionBody': "Who wrote the famous novel 'Moby Dick'?", 'questionId': 11}, {'options': ['Mercury', 'Venus', 'Earth', 'Mars'], 'questionBody': 'Which planet is closest to the sun?', 'questionId': 12}, {'options': ['Tim Berners-Lee', 'Larry Page', 'Sergey Brin', 'Steve Jobs'], 'questionBody': 'Who invented the World Wide Web?', 'questionId': 13}, {'options': ['Stapes', 'Incus', 'Malleus', 'Capitate'], 'questionBody': 'What is the smallest bone in the human body?', 'questionId': 14}, {'options': ['Athens', 'Paris', 'London', 'Rome'], 'questionBody': 'Which city hosted the 1896 Summer Olympics?', 'questionId': 15}, {'options': ['Rabindranath Tagore', 'Bankim Chandra Chattopadhyay', 'Sarojini Naidu', 'Muhammad Iqbal'], 'questionBody': "Who wrote the Indian national anthem 'Jana Gana Mana'?", 'questionId': 16}, {'options': ['Pascal', 'Bar', 'Torr', 'Atmosphere'], 'questionBody': 'What is the SI unit of pressure?', 'questionId': 17}, {'options': ['9', '11', '15', '23'], 'questionBody': 'Which of these numbers is a prime number?', 'questionId': 
# 18}, {'options': ['Arctic Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Southern Ocean'], 'questionBody': 'What is the smallest ocean in the world?', 'questionId': 19}, {'options': ['J.K. Rowling', 'Stephen King', 'Dan Brown', 'Nora Roberts'], 'questionBody': 'Who is the author of the Harry Potter book series?', 'questionId': 20}]

# import json

# data = {
#     "userId": "userid",
#     "test1": {
#         "question_responses": [
#             {
#                 "question_id": "question_id_1",
#                 "answer": "answer_id_1",
#                 "correct_answer": "correct_answer_1"
#             },
#             {
#                 "question_id": "question_id_2",
#                 "answer": "correct_answer_2",
#                 "correct_answer": "correct_answer_2"
#             },
#             {
#                 "question_id": "question_id_3",
#                 "answer": "answer_id_3",
#                 "correct_answer": "correct_answer_3"
#             }
#         ]
#     }
# }

# def calculate_score(data):  
#     score = 0

#     for response in data["test1"]["question_responses"]:
#         if response["answer"] == response["correct_answer"]:
#             response["score"] = 3
#             score += 3
#         else:
#             response["score"] = -1
#             score -= 1

#     data["test1"]["final_score"] = score
#     return data

# result = calculate_score(data)
# result_json = json.dumps(result, indent=2)
# print(result_json)


