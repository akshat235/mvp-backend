from flask_sqlalchemy import SQLAlchemy
from mongoengine import Document, StringField, ListField, IntField, EmbeddedDocument, EmbeddedDocumentField

db = SQLAlchemy()

class UserAuth(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


class UserData(db.Model):
    userId = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    password = db.Column(db.String(255), nullable=False)



class Question(Document):
  questionId = IntField()
  questionBody = StringField()
  options = ListField(StringField())
  correctAnswer = StringField()
  
  meta = {'collection': 'Question'}


class Question_Response(EmbeddedDocument):
    correctAnswer = StringField()
    id = StringField()
    options = ListField(StringField())
    questionBody = StringField()
    questionId = IntField()
    selectedOption = StringField()
    score = IntField()
class TestData(EmbeddedDocument):
    test_number = IntField()
    responses = ListField(EmbeddedDocumentField(Question_Response))

# class TestResponse(Document):
#     userid = StringField()
#     tests = ListField(EmbeddedDocumentField(TestData))
    
#     meta = {
#         'collection': 'test_responses'
#     }
# class TestResponse(Document):
#     userId = StringField()
#     tests = ListField(EmbeddedDocumentField(TestData))
#     total_score = IntField()  # Add total_score field

#     meta = {
#         'collection': 'test_responses'
#     }


class TestResponse(Document):
    userId = StringField()
    responses = ListField(EmbeddedDocumentField(Question_Response))
    total_score = IntField()

    meta = {
        'collection': 'test_responses'
    }

class SectionQuestionResponse(EmbeddedDocument):
    questionid = StringField()
    correctans = StringField()
    optionSelected = StringField()

class Submission(EmbeddedDocument):
    VARC = ListField(EmbeddedDocumentField(SectionQuestionResponse))
    QUANT = ListField(EmbeddedDocumentField(SectionQuestionResponse))
    DILR = ListField(EmbeddedDocumentField(SectionQuestionResponse))

class TestResponseWSection(Document):
    userId = StringField()
    submission = EmbeddedDocumentField(Submission)
    test_number= IntField()
    score_varc = IntField()
    score_quant = IntField()
    score_dilr = IntField()
    total_score = IntField()

    meta = {
        'collection': 'response_with_section'  
    }