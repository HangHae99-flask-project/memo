from flask import Blueprint, render_template, jsonify,request
from pymongo import MongoClient
from datetime import datetime, timedelta, time
from bson import ObjectId


client = MongoClient('mongodb+srv://sparta:k1716k@sparta.cwrvz74.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

read = Blueprint('read', __name__)

@read.route('/read/<dd>', methods=["POST"])
def read_one(dd):
    memo = db.memo.find_one({'_id': ObjectId(dd)})
    future_memo = db.futurememo.find_one({'_id' : ObjectId(dd)})
    print(dd)
    if memo :
        content = memo['content']
        print(str(memo['content']))
    elif future_memo:
        content = future_memo['content']
        print(str(future_memo['content']))

    return jsonify({'content': content})

@read.route('/read', methods=["POST"])
def read_list():
    param_value = request.form.get('memoid')
    print(param_value)


    user_id = request.form['id_give']
    print(user_id)


    all_infor = list(db.memo.find({'userid' : user_id},{}))
    all_future = list(db.futurememo.find({'userid' : user_id},{} ))
    
    today = datetime.now()

    data = []

    for t in all_infor:
        t['_id'] = str(ObjectId(t['_id']))
    
    for ist in all_future:
        datetime_obj = datetime.fromisoformat(str(ist['timeday']))
        if datetime_obj < today or datetime == today:
            ist['_id'] = str(ObjectId(ist['_id']))
            data.append(ist)
        
        

    return jsonify({'result': all_infor, 'result1' : data})