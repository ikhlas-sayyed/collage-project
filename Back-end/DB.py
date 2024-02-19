import os
import datetime
from mongoengine import connect, Document, StringField, IntField, DateTimeField

# Connect to MongoDB
connect(os.environ['DATABASE_NAME'], host=os.environ['DATABASE_URI'])

class Student(Document):
    name = StringField(required=True)
    roll_no = IntField(required=True)
    div = StringField(required=True)
    class_no:IntField(required=True)
    en_no:IntField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)

class User(Document):
    user_id=StringField(required=True,unique=True)
    name= StringField(required=True)
    number=IntField(required=True)
    password=StringField(required=True)

class Attendance(Document):
    subject=StringField(required=True)
    div=StringField(required=True)
    present=[
        IntField(required=True)
    ]
    absent=[
        IntField(required=True)
    ]
