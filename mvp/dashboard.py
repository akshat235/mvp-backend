from models import Question, Question_Response, TestResponseWSection
from flask import Flask, request, jsonify, Blueprint
from mongoengine import DoesNotExist
import mongoengine
import random, os, sys
import urllib.parse


dashboard_bp = Blueprint("dashboard", __name__ )  
mongoengine.connect('cat_exam', host='mongodb://localhost:27017')

@dashboard_bp.route('/test_data/', methods=['GET'])
def get_test_responses():
    try:
        # userid = urllib.parse.unquote(enuserid)
        # print(userid)
        userid = request.args.get('userid')
        print(userid)
        # userid = urllib.parse.unquote(userid)
        test_responses = TestResponseWSection.objects()
        # print(test_responses)
        response_data = []
        for test_response in test_responses:
            data = {
                'finalscore': test_response.total_score,
                'VARCscore': test_response.score_varc,
                'QUANTscore': test_response.score_quant,
                'DILRscore': test_response.score_dilr,
                'percentagecorrect': round((test_response.total_score*100) / 48, 2)
            }
            response_data.append(data)

        return jsonify(response_data), 200
    except TestResponseWSection.DoesNotExist:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return jsonify({"message": "Test data not found for the specified userid."}), 404

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(e)
        return jsonify({"message": f"An error occurred while fetching data: {str(e)}"}), 500





# def get_test_responses():
#     try:

#         test_responses = TestResponse.objects()
#         response_data = []
#         for test_response in test_responses:
#             response_data.append({
#                 'userId': test_response.userId,
#                 'responses': [
#                     {
#                         'correctAnswer': response.correctAnswer,
#                         'id': response.id,
#                         'options': response.options,
#                         'questionBody': response.questionBody,
#                         'questionId': response.questionId,
#                         'selectedOption': response.selectedOption,
#                         'score': response.score,
#                     }
#                     for response in test_response.responses
#                 ],
#                 'total_score': test_response.total_score
#             })
#         return jsonify(response_data), 200

#     except Exception as e:
#         return jsonify({"message": f"An error occurred while fetching data: {str(e)}"}), 500
