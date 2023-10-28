from models import Question, Question_Response, TestResponseWSection
from flask import Flask, request, jsonify, Blueprint, session, make_response, send_file
from mongoengine import DoesNotExist
import mongoengine
import random, os, sys
import matplotlib.pyplot as plt
import numpy as np



dashboard_bp = Blueprint("dashboard", __name__ )  
mongoengine.connect('cat_exam', host='mongodb://localhost:27017')
uID=""
# global loggedInUserId

@dashboard_bp.route('/send_userid', methods=['POST'])
def get_loggedin_userid():
    if request.method == 'POST':
        try:
            data = request.get_json()
            userID = data.get('userID')
            # print(userID)

            if userID is not None:
                global uID
                uID=userID
                return jsonify({"message": "User ID set in the session."})
            else:
                return jsonify({"error": "Invalid or missing 'userID' in the request data."}), 400

        except Exception as e:
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return jsonify({"error": "An error occurred while processing the request."}), 500
    else:
        return jsonify({"error": "Unsupported HTTP method."}), 405


@dashboard_bp.route('/test_data', methods=['GET'])
def get_test_responses():
    try:
        data=[]
        # loggedinuser_id = session.get("loggedInUserId")
        # loggedinuser_Id = request.cookies.get('user_id')
        global uID
        loggedinuser_Id = uID
        test_responses = TestResponseWSection.objects(userId=loggedinuser_Id)
        print(len(test_responses))
        print("useridfrom test respone func", loggedinuser_Id)
        response_data = []
        for test_response in test_responses:
            data = {
                    'test_number': test_response.test_number,
                    'finalscore': test_response.total_score,
                    'VARCscore': test_response.score_varc,
                    'QUANTscore': test_response.score_quant,
                    'DILRscore': test_response.score_dilr,
                    'percentagecorrect': round((test_response.total_score*100) / 48, 2)
            }
            response_data.append(data)
        # print("LENGHT", response_data)
        growth_percentages = []
        for i in range(1, len(response_data)):
            current_score = response_data[i]['finalscore']
            previous_score = response_data[i - 1]['finalscore']
            # if previous_score:
            week_on_week_growth = ((current_score - previous_score) / previous_score) * 100
            growth_percentages.append(week_on_week_growth)
        average_growth_percentage = sum(growth_percentages) / len(growth_percentages) if growth_percentages else 0
        average_growth_percentage = round(average_growth_percentage,2)

        # print("GROWTH PERCENTAGE ->", growth_percentages)
        response_data.append({'average_growth':average_growth_percentage})
        response_data.append({'last_weeks_growth':round(growth_percentages[-1],2)})


        print("CONSOLE DATA _________________-----_____", response_data)

        test_numbers = [item['test_number'] for item in response_data[:-2]]
        total_scores = [item['finalscore'] for item in response_data[:-2]]
        x_smooth = np.linspace(min(test_numbers), max(test_numbers), 100)
        y_smooth = np.interp(x_smooth, test_numbers, total_scores)
        plt.figure(figsize=(6, 4), facecolor='lightgrey') 
        plt.plot(x_smooth, y_smooth, linestyle='-', color='blue')
        plt.xlabel('Test Number')
        plt.ylabel('Total Score')
        plt.title(' ')
        plt.grid(False)
        plt.xticks(test_numbers)
        filename = 'graphs/test_number_vs_total_score.png'
        if os.path.exists(filename):
            os.remove(filename)  
        plt.savefig(filename, format='png', dpi=300)

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


@dashboard_bp.route('/get_image')
def get_image():
    return send_file('graphs/test_number_vs_total_score.png', as_attachment=True)


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
