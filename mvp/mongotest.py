import pymongo
import mongoengine

# mongoengine.register_connection(
#     alias='default',
#     name='response',
#     host='mongodb+srv://sequio:nkY9KPEPZmNhBYYx@cluster0.jyovip1.mongodb.net/?retryWrites=true&w=majority/user')

mongoengine.register_connection(
    alias='default',
    name='response',
    host='mongodb+srv://sequio:nkY9KPEPZmNhBYYx@cluster0.jyovip1.mongodb.net/user')


# mongo_url = "mongodb+srv://sequio:nkY9KPEPZmNhBYYx@cluster0.jyovip1.mongodb.net/?retryWrites=true&w=majority/user"

# # Replace 'username' and 'password' with your actual MongoDB username and password

# try:
#     # Attempt to connect to the MongoDB server
#     connection = mongoengine.get_connection(alias='default')
    
#     # Check if the connection was successful
#     if connection.server_info():
#         print("Successfully connected to MongoDB using MongoEngine.")
#     else:
#         print("Failed to connect to MongoDB using MongoEngine.")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")


data = {
  "userId": "1231",
  "submission": {
    "VARC": [
      {
        "questionid": "0",
        "correctans": "\nThe Stoic influences can be seen in multiple religions",
        "optionSelected": ""
      },
      {
        "questionid": "1",
        "correctans": "Marcus Aurelius was one of the leaders of the Roman army",
        "optionSelected": ""
      },
      {
        "questionid": "2",
        "correctans": "Meditation allows certain out-of-body experiences that permit us to gain the distance necessary to control our emotions.",
        "optionSelected": ""
      },
      {
        "questionid": "3",
        "correctans": "In the Epicurean view, indulging in simple pleasures is not desirable.",
        "optionSelected": ""
      },
      {
        "questionid": "4",
        "correctans": "Technology, laws, and customs are not unlike each other if considered as institutions",
        "optionSelected": ""
      },
      {
        "questionid": "5",
        "correctans": "Masses are organised in patterns set by Foucault’s prisons and Habermas’ public sphere.",
        "optionSelected": ""
      },
      {
        "questionid": "6",
        "correctans": "Technologies form the environmental context and shape the contours of human society.",
        "optionSelected": ""
      },
      {
        "questionid": "7",
        "correctans": "technologies seek to privilege certain dimensions of human nature at a high cost to lived nature.",
        "optionSelected": ""
      },
      {
        "questionid": "8",
        "correctans": "The passage discusses the evolution of theories of the Undead from primitive thinking to the Age of Enlightenment",
        "optionSelected": ""
      },
      {
        "questionid": "9",
        "correctans": "Human beings conceptualise the Undead as possessing abnormal features",
        "optionSelected": ""
      },
      {
        "questionid": "10",
        "correctans": "the transition from the Middle Ages to the Age of Enlightenment saw new theories of the Undead",
        "optionSelected": ""
      },
      {
        "questionid": "11",
        "correctans": "Mankind’s early years were marked by a belief in the existence of eerie creatures that were neither quite alive nor dead",
        "optionSelected": "Mankind’s primal years were marked by creatures alive with eerie whispers, but seen only in the darkness"
      },
      {
        "questionid": "12",
        "correctans": "Both are continually undergoing restoration.",
        "optionSelected": ""
      },
      {
        "questionid": "13",
        "correctans": "it discourages them from carrying out human cloning",
        "optionSelected": ""
      },
      {
        "questionid": "14",
        "correctans": "A 17th century French artist who adhered to a Christian worldview would need to be completely true to the original intent of a painting when restoring it.",
        "optionSelected": ""
      },
      {
        "questionid": "15",
        "correctans": "Pablo Picasso’s painting of Vincent van Gogh’s original painting, identical in every respect.",
        "optionSelected": "Pablo Picasso’s miniaturised, but otherwise faithful and accurate painting of Vincent van Gogh’s original painting."
      }
    ],
    "QUANT": [
      {
        "questionid": "0",
        "correctans": "\nThe Stoic influences can be seen in multiple religions",
        "optionSelected": ""
      },
      {
        "questionid": "1",
        "correctans": "Marcus Aurelius was one of the leaders of the Roman army",
        "optionSelected": ""
      },
      {
        "questionid": "2",
        "correctans": "Meditation allows certain out-of-body experiences that permit us to gain the distance necessary to control our emotions.",
        "optionSelected": ""
      },
      {
        "questionid": "3",
        "correctans": "In the Epicurean view, indulging in simple pleasures is not desirable.",
        "optionSelected": ""
      },
      {
        "questionid": "4",
        "correctans": "Technology, laws, and customs are not unlike each other if considered as institutions",
        "optionSelected": ""
      },
      {
        "questionid": "5",
        "correctans": "Masses are organised in patterns set by Foucault’s prisons and Habermas’ public sphere.",
        "optionSelected": ""
      },
      {
        "questionid": "6",
        "correctans": "Technologies form the environmental context and shape the contours of human society.",
        "optionSelected": "Technologies form the environmental context and shape the contours of human society."
      },
      {
        "questionid": "7",
        "correctans": "technologies seek to privilege certain dimensions of human nature at a high cost to lived nature.",
        "optionSelected": ""
      },
      {
        "questionid": "8",
        "correctans": "The passage discusses the evolution of theories of the Undead from primitive thinking to the Age of Enlightenment",
        "optionSelected": "The writer describes the ways in which the Undead come to be associated with Shamans and the practice of magic"
      },
      {
        "questionid": "9",
        "correctans": "Human beings conceptualise the Undead as possessing abnormal features",
        "optionSelected": ""
      },
      {
        "questionid": "10",
        "correctans": "the transition from the Middle Ages to the Age of Enlightenment saw new theories of the Undead",
        "optionSelected": ""
      },
      {
        "questionid": "11",
        "correctans": "Mankind’s early years were marked by a belief in the existence of eerie creatures that were neither quite alive nor dead",
        "optionSelected": ""
      },
      {
        "questionid": "12",
        "correctans": "Both are continually undergoing restoration.",
        "optionSelected": ""
      },
      {
        "questionid": "13",
        "correctans": "it discourages them from carrying out human cloning",
        "optionSelected": ""
      },
      {
        "questionid": "14",
        "correctans": "A 17th century French artist who adhered to a Christian worldview would need to be completely true to the original intent of a painting when restoring it.",
        "optionSelected": ""
      },
      {
        "questionid": "15",
        "correctans": "Pablo Picasso’s painting of Vincent van Gogh’s original painting, identical in every respect.",
        "optionSelected": "Pablo Picasso’s photograph of Vincent van Gogh’s original painting, printed to exactly the same scale"
      }
    ],
    "DILR": [
      {
        "questionid": "0",
        "correctans": "\nThe Stoic influences can be seen in multiple religions",
        "optionSelected": ""
      },
      {
        "questionid": "1",
        "correctans": "Marcus Aurelius was one of the leaders of the Roman army",
        "optionSelected": ""
      },
      {
        "questionid": "2",
        "correctans": "Meditation allows certain out-of-body experiences that permit us to gain the distance necessary to control our emotions.",
        "optionSelected": ""
      },
      {
        "questionid": "3",
        "correctans": "In the Epicurean view, indulging in simple pleasures is not desirable.",
        "optionSelected": ""
      },
      {
        "questionid": "4",
        "correctans": "Technology, laws, and customs are not unlike each other if considered as institutions",
        "optionSelected": ""
      },
      {
        "questionid": "5",
        "correctans": "Masses are organised in patterns set by Foucault’s prisons and Habermas’ public sphere.",
        "optionSelected": ""
      },
      {
        "questionid": "6",
        "correctans": "Technologies form the environmental context and shape the contours of human society.",
        "optionSelected": ""
      },
      {
        "questionid": "7",
        "correctans": "technologies seek to privilege certain dimensions of human nature at a high cost to lived nature.",
        "optionSelected": ""
      },
      {
        "questionid": "8",
        "correctans": "The passage discusses the evolution of theories of the Undead from primitive thinking to the Age of Enlightenment",
        "optionSelected": ""
      },
      {
        "questionid": "9",
        "correctans": "Human beings conceptualise the Undead as possessing abnormal features",
        "optionSelected": ""
      },
      {
        "questionid": "10",
        "correctans": "the transition from the Middle Ages to the Age of Enlightenment saw new theories of the Undead",
        "optionSelected": ""
      },
      {
        "questionid": "11",
        "correctans": "Mankind’s early years were marked by a belief in the existence of eerie creatures that were neither quite alive nor dead",
        "optionSelected": "Long ago, eerie creatures used to whisper in the primal darkness that they were not quite dead."
      },
      {
        "questionid": "12",
        "correctans": "Both are continually undergoing restoration.",
        "optionSelected": "Both were built as places of worship."
      },
      {
        "questionid": "13",
        "correctans": "it discourages them from carrying out human cloning",
        "optionSelected": "it discourages them from simultaneous displays of multiple copies of a painting."
      },
      {
        "questionid": "14",
        "correctans": "A 17th century French artist who adhered to a Christian worldview would need to be completely true to the original intent of a painting when restoring it.",
        "optionSelected": "A 17th century British painter would have no problem adding personal touches when restoring an ancient Roman painting."
      },
      {
        "questionid": "15",
        "correctans": "Pablo Picasso’s painting of Vincent van Gogh’s original painting, identical in every respect.",
        "optionSelected": "Pablo Picasso’s photograph of Vincent van Gogh’s original painting, printed to exactly the same scale"
      }
    ]
  },
  "test_number": 1,
  "date": "26/10/2023",
  "time": "02:53",
  "score_varc": 6,
  "score_quant": 1,
  "score_dilr": 0,
  "total_score": 7
}


class User(mongoengine.Document):
    # _id = mongoengine.StringField(required=True)
    userId = mongoengine.StringField(required=True)
    submission = mongoengine.DictField(required=True)
    test_number = mongoengine.IntField(required=True)
    date = mongoengine.DateTimeField(required=True)
    time = mongoengine.StringField(required=True)
    score_varc = mongoengine.IntField(required=True)
    score_quant = mongoengine.IntField(required=True)
    score_dilr = mongoengine.IntField(required=True)
    total_score = mongoengine.IntField(required=True)


new_submission = User(**data)
new_submission.save()