from models import Question, Question_Response, TestResponse
from flask import Flask, request, jsonify, Blueprint
from mongoengine import DoesNotExist
import mongoengine
import random


dashboard_bp = Blueprint("dashboard", __name__ )  
mongoengine.connect('cat_exam', host='mongodb://localhost:27017')

@dashboard_bp.route('/get_test_responses', methods=['GET'])

def get_test_responses():
    try:

        test_responses = TestResponse.objects()
        response_data = []
        for test_response in test_responses:
            response_data.append({
                'userId': test_response.userId,
                'responses': [
                    {
                        'correctAnswer': response.correctAnswer,
                        'id': response.id,
                        'options': response.options,
                        'questionBody': response.questionBody,
                        'questionId': response.questionId,
                        'selectedOption': response.selectedOption,
                        'score': response.score,
                    }
                    for response in test_response.responses
                ],
                'total_score': test_response.total_score
            })
        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"message": f"An error occurred while fetching data: {str(e)}"}), 500
