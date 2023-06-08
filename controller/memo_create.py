from flask import Blueprint, render_template, jsonify,request,redirect,url_for
from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient('mongodb+srv://sparta:k1716k@sparta.cwrvz74.mongodb.net/?retryWrites=true&w=majority', )
db = client.dbsparta

create = Blueprint('create', __name__)

@create.route('/create')
def home():
    
    cookie_value = request.cookies.get('userid')
    if cookie_value:
        return render_template('page/create.html')
    return redirect(url_for('main.register'))
    

@create.route('/create/now', methods=["POST"])
def now():
    title = request.form['title']
    userid = request.form['userid']
    print(userid)
    if not title:
        msg='제목을 입력해주세요.'
    else:
        now = datetime.now()
        doc = {
            'title': title,
            'userid': userid, # cookie 나 그런곳에서 가져올것.
            'content':'',
            'create_day':now,
            'update_day':'',
        }
        db.memo.insert_one(doc)
        msg = '성공적으로 메모 추가하였습니다.'

    return jsonify({'msg': msg})

@create.route('/create/future', methods=["POST"])
def future():
    title = request.form['title']
    content = request.form['content']
    day = request.form['day'] 
    userid = request.form['userid'] 
    
    if not title:
        msg='제목을 입력해주세요.'
    elif not content:
        msg='내용을 입력해주세요.'
    elif not day:
        msg='날짜를 설정해주세요.'
    else:
        now = datetime.now()
        nowday = now + timedelta(days=int(day))
        doc = {
            'title': title,
            'userid': userid, # cookie 나 그런곳에서 가져올것.
            'content': content,
            'timeday':nowday,
            'create_day':now,
            'update_day':'',
        }
        db.futurememo.insert_one(doc)
        msg = '성공적으로 메모 추가하였습니다.'

    return jsonify({'msg': msg})