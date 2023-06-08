from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from flask_mail import Mail, Message
from controller import main, memo_create, memo_update, memo_read, sign_up, memo_delete,log_in
import random 



client = MongoClient('mongodb+srv://sparta:k1716k@sparta.cwrvz74.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.naver.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ty_ty123'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

#이메일 인증
@app.route('/api/email', methods=["POST"])
def test():
    email = request.form['email']
    print(random.randint(1,9))
    randomStr = str(random.randint(1,9))
    for i in range(5):
        randomStr+=str(random.randint(1,9))

    doc = {
        'email' : email,
        'successKey': randomStr
    }
    db.email.insert_one(doc)

    send_email(email,randomStr)
    return jsonify({'msg': '이메일이 성공적으로 전송하였습니다.'})

def send_email( receiver, random):
    
    mail = Mail(app)
    msg = Message('제목', sender = 'ty_ty123@naver.com', recipients = [receiver])
    msg.body = '코드 : '+random
    mail.send(msg)


#라우트 공간
app.register_blueprint(main.main, url_prefix="/")
app.register_blueprint(memo_create.create, url_prefix="/api")
app.register_blueprint(memo_read.read, url_prefix="/api")
app.register_blueprint(memo_update.update, url_prefix="/api")
app.register_blueprint(sign_up.signup, url_prefix="/api")
app.register_blueprint(memo_delete.delete, url_prefix="/api")
app.register_blueprint(log_in.log_in, url_prefix="/")

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)