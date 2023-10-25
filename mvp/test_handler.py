from models import Question, Question_Response, TestResponse
from flask import Flask, request, jsonify, Blueprint
from mongoengine import DoesNotExist
import mongoengine
import random


test_bp = Blueprint("test_handler", __name__ )  
mongoengine.connect('cat_exam', host='mongodb://localhost:27017')

def calculate_score(response_data):
    score = 0
    for question in response_data:
        if question['correctAnswer'] == question['selectedOption']:
            score = 3
        else:
            score = -1
        question['score'] = score


@test_bp.route('/questions')
def get_questions():
    try:
        qq = Question.objects()
        questions_json = [
            {
                'id': str(question.id),
                'questionId': question.questionId,
                'questionBody': question.questionBody,
                'options': question.options,
                'correctAnswer': question.correctAnswer
            }
            for question in qq
        ]
        # questions_without_ans = [
        #     {
        #         'questionId': question.questionId,
        #         'questionBody': question.questionBody,
        #         'options': question.options
        #     }
        #     for question in qq
        # ]
        # questions_15 =random.sample(questions_without_ans,15)
        return jsonify(questions_json), 200
    except DoesNotExist:
        return jsonify({'error': 'No questions found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@test_bp.route('/submitresponse', methods=['POST'])
def save_test_response():
    if request.method == 'POST':
        data = request.get_json()
        # print(data)
        if not data:
            return jsonify({"message": "Invalid data format"}), 400 
        try:
            for response in data['responses']:
                calculate_score(response['response_data'])

            total_score = sum(question['score'] for question in data['responses'][0]['response_data'])
            data['responses'][0]['total_score'] = total_score
            
            test_response = TestResponse(
                    userId=data['userId'],
                    responses=[Question_Response(**response_data) for response_data in data['responses'][0]['response_data']],
                    total_score=data['responses'][0]['total_score']
                )
            test_response.save()
            return jsonify({"message": "Test response submitted successfully"}), 200

        except Exception as e:
            print(e)
            return jsonify({"message": "An error occurred while processing the request"}), 500  

    return jsonify({"message": "Invalid request method"}), 405