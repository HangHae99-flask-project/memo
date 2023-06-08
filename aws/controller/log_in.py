from datetime import datetime, timedelta
from flask import Blueprint,redirect, render_template, jsonify,request, session, redirect, url_for
from pymongo import MongoClient

log_in = Blueprint('log_in', __name__)

client = MongoClient('mongodb+srv://sparta:k1716k@sparta.cwrvz74.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@log_in.route('/login', methods=["POST"])
def id_pw_check():
    userid_receive = request.form['userid_give']
    userpw_receive = request.form['userpw_give']
    user_info = db.users.find_one({'userid': userid_receive}, {'_id': False})
    
   #  print(str(user_info))
    if user_info and user_info['userpw'] == userpw_receive :
        print('success')
        print(userid_receive, userpw_receive)
        return jsonify({'result': '로그인에 성공하셨습니다.', 'check':'true','userid': userid_receive})
    else:
        print('fail')
        print(userid_receive, userpw_receive)
        return jsonify({'result': '로그인에 실패하였습니다.','check':'false'})
