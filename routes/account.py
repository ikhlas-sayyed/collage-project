import os
from flask import Blueprint ,request, jsonify
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from DB import Student,User

account = Blueprint('account', __name__)

@account.route('/add_student',methods=['POST'])
def add_student():
    data=request.json
    div=['A','B','C','D','E','F']
    if ("name" in data and "roll_no" in data and "div" in data and "class_no" in data) :
        if (len(data['name'])>8 and int(data['roll_no'])>0 and data['div'] in div and int(data['class_no'])>0 and int(data['class_no'])<5):
            student=Student(name=data['name'],roll_no=data['roll_no'],div=data['div'],class_no=data['class_no'])
            student.save()
            return jsonify({"success":True,"message": "student add successfully"})
        else:
            return jsonify({"success":False,"message":"Incompolete Data"})
    else:
        return jsonify({"success":False,"message":"data is Undefinde"})

account.route('/login')
def login():
    data=request.json
    if("user_id" in data and "password" in data):
        user=User.objects(user_id=data[user_id],password=data['password'])
        if(user):
            pass