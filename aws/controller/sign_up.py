from flask import Blueprint, render_template, jsonify,request
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb+srv://sparta:k1716k@sparta.cwrvz74.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

signup = Blueprint('signup', __name__)


@signup.route('/successkey', methods=["POST"])
def emailSuccesskey():
    email = request.form['email']
    successkey = request.form['successkey']
    msg = 'false'
    data_msg = '이메일 인증 코드가 맞지 않습니다.'

    emailDb = db.email.find_one({'email':email},{'_id':False})
    if emailDb['successKey'] == successkey:
        msg = 'true'
        data_msg = '이메일 인증이 완료되었습니다.'
    db.email.delete_one({'email': email})

    return jsonify({'msg': msg,'data_msg':data_msg})



@signup.route('/register', methods=["POST"])
def register():
    id = request.form['id']
    pw = request.form['pw']
    nickname = request.form['nickname']
    email = request.form['email']
    now = datetime.now()

    checkId = db.users.find_one({"userid":id})
    print(checkId)
    if not checkId:

        if len(id) >=5 and len(id) <=10:
            if len(pw) >= 8 and len(pw) <= 15:
                if pw.isalnum():
                    msg = "비밀번호에는 특수문자가 필요합니다."
                else:
                    doc = {
                        "userid" : id,
                        "userpw" : pw,
                        "nickname" : nickname,
                        "email" : email,
                        "create_day" : now,
                        "update_day" : ''
                    }

                    db.users.insert_one(doc)
                    msg = '회원가입이 성공적으로 가입하였습니다.'
            else:
                msg = "비밀번호의 글자 길이가 짧거나 길쭉합니다."
        else:
            msg = "아이디의 글자 길이가 짧거나 길쭉합니다."
    else:
        msg = "동일한 아이디가 존재합니다."


    
    
    return jsonify({'msg': msg})
