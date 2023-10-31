from models import Question, Question_Response, TestResponse, SectionQuestionResponse, TestResponseWSection, Submission
from flask import Flask, request, jsonify, Blueprint
from mongoengine import DoesNotExist
import mongoengine
import random, os, sys
from datetime import datetime
from flask_cors import CORS, cross_origin
from flask import make_response



test_bp = Blueprint("test_handler", __name__ )
#CORS(test_bp)  
mongoengine.connect('cat_exam', host='mongodb://localhost:27017') ## need to change connection string. It is connecting to local host

# def handle_options(response):
    # origin = request.headers.get('Origin')
    # if request.method == 'OPTIONS':
        # response = make_response()
        # response.headers.add('Access-Control-Allow-Credentials', 'true')
        # response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        # response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
        # response.headers.add('Access-Control-Allow-Methods',
                            # 'GET, POST, OPTIONS, PUT, PATCH, DELETE')
        # if origin:
            # response.headers.add('Access-Control-Allow-Origin', origin)
    # else:
        # response.headers.add('Access-Control-Allow-Credentials', True)
        # if origin:
            # response.headers.add('Access-Control-Allow-Origin', origin)

        # return response,200
@test_bp.route('/submitresponse', methods=['OPTIONS'])
@test_bp.route("/get_paper_number", methods = ['OPTIONS'])
@test_bp.after_request
def handle_options():
    origin = request.headers.get('Origin')
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
        response.headers.add('Access-Control-Allow-Methods',
                            'GET, POST, OPTIONS, PUT, PATCH, DELETE')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)
        else:
            response.headers.add('Access-Control-Allow-Credentials', 'true')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)
        
    return response




def _corsify_actual_response(response):
    #response.headers.add("Access-Control-Allow-Origin", "http://sequio-mvp.rf.gd/")
    return response

def calculate_score(response_data):
    score = 0
    for question in response_data:
        if question['correctAnswer'] == question['selectedOption']:
            score = 3
        else:
            score = -1
        question['score'] = score


def get_test_number(userID):
    test_responses = TestResponseWSection.objects(userId=userID)
    return len(test_responses) + 1


user_ID=None

@test_bp.route("/get_paper_number", methods = ['POST','GET'])
@cross_origin()
def get_paper_number():
    global user_ID
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'userID' not in data:
            return jsonify({"error": "Invalid data format or missing 'userID'"}), 400
        # global user_ID
        user_ID = data['userID']
        print(user_ID)
        return _corsify_actual_response(jsonify({"message": "Received userID"})), 200

    if request.method == 'GET':
        try:
            # global userID
            print(user_ID)
            test_responses = TestResponseWSection.objects(userId=user_ID)
            print(len(test_responses))
            return _corsify_actual_response(jsonify({'paper_number': len(test_responses)})), 200
        except Exception as e:
            # Log the exception details for debugging
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"An error occurred: {exc_type} in {fname} at line {exc_tb.tb_lineno}")
            return _corsify_actual_response(jsonify({"error": "An error occurred while processing the request."})), 500

    return _corsify_actual_response(jsonify({"error": "Unsupported request method"})), 405



# @test_bp.route('/send_userid', methods=['POST'])
# def get_loggedin_userid():
#     if request.method == 'POST':
#         try:
#             data = request.get_json()
#             userID = data.get('userID')
#             # print(userID)
#             if userID is not None:
#                 global uID
#                 uID=userID
#                 print(uID)
#                 return jsonify({"message": "User ID set in the session."})
#             else:
#                 return jsonify({"error": "Invalid or missing 'userID' in the request data."}), 400

#         except Exception as e:
#             print(e)
#             exc_type, exc_obj, exc_tb = sys.exc_info()
#             fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#             print(exc_type, fname, exc_tb.tb_lineno)
#             return jsonify({"error": "An error occurred while processing the request."}), 500
#     else:
#         return jsonify({"error": "Unsupported HTTP method."}), 405



# @test_bp.route('/questions')
# def get_questions():
    
#     try:
#         qq = Question.objects()
#         questions_json = [
#             {
#                 'id': str(question.id),
#                 'questionId': question.questionId,
#                 'questionBody': question.questionBody,
#                 'options': question.options,
#                 'correctAnswer': question.correctAnswer
#             }
#             for question in qq
#         ]

#         return jsonify(questions_json), 200
#     except DoesNotExist:
#         return jsonify({'error': 'No questions found'}), 404
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


@test_bp.route('/submitresponse', methods=['POST'])
@cross_origin()
def save_test_response():
    if request.method == 'POST':
        data = request.get_json()
        # print(data)
        
        if not data:
            return jsonify({"message": "Invalid data format"}), 400 
        try:
            current_datetime = datetime.now()
            userid = data.get('userId')
            submission_data = data.get('submission')
            test_no = get_test_number(userid)

            test_response_instance = TestResponseWSection(
                userId=userid,
                submission = Submission(
                    VARC=[SectionQuestionResponse(
                        questionid=str(question.get('questionid')),
                        correctans=question.get('correctans'),
                        optionSelected=question.get('optionSelected')
                    ) for question in submission_data.get('VARC')[0]],
                    QUANT=[SectionQuestionResponse(
                        questionid=str(question.get('questionid')),
                        correctans=question.get('correctans'),
                        optionSelected=question.get('optionSelected')
                    ) for question in submission_data.get('QUANT')[0]],
                    DILR=[SectionQuestionResponse(
                        questionid=str(question.get('questionid')),
                        correctans=question.get('correctans'),
                        optionSelected=question.get('optionSelected')
                    ) for question in submission_data.get('DILR')[0]]
                ),
                test_number=test_no,
                date = current_datetime.strftime("%d/%m/%Y"),
                time = current_datetime.strftime("%H:%M")
            )
            test_response_instance.score_varc = sum(
                1 for question in test_response_instance.submission.VARC
                if question.correctans == question.optionSelected
            )

            test_response_instance.score_quant = sum(
                1 for question in test_response_instance.submission.QUANT
                if question.correctans == question.optionSelected
            )

            test_response_instance.score_dilr = sum(
                1 for question in test_response_instance.submission.DILR
                if question.correctans == question.optionSelected
            )

            total_score = (
                test_response_instance.score_varc
                + test_response_instance.score_quant
                + test_response_instance.score_dilr
            )
            test_response_instance.total_score = total_score

            test_response_instance.save()
            return _corsify_actual_response(jsonify({"message": "Test response submitted successfully"})), 200

        except Exception as e:
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return _corsify_actual_response(jsonify({"message": f"Error: {str(e)}"})), 500 

    return _corsify_actual_response(jsonify({"message": "Invalid request method"})), 405
    






# @test_bp.route('/submitresponse', methods=['POST'])
# def save_test_response():
#     if request.method == 'POST':
#         data = request.get_json()
#         # print(data)
#         if not data:
#             return jsonify({"message": "Invalid data format"}), 400 
#         try:
            
#             for response in data['responses']:
#                 calculate_score(response['response_data'])

#             total_score = sum(question['score'] for question in data['responses'][0]['response_data'])
#             data['responses'][0]['total_score'] = total_score
            
#             test_response = TestResponse(
#                     userId=data['userId'],
#                     responses=[Question_Response(**response_data) for response_data in data['responses'][0]['response_data']],
#                     total_score=data['responses'][0]['total_score']
#                 )
#             test_response.save()
#             return jsonify({"message": "Test response submitted successfully"}), 200

#         except Exception as e:
#             print(e)
#             return jsonify({"message": "An error occurred while processing the request"}), 500  

#     return jsonify({"message": "Invalid request method"}), 405