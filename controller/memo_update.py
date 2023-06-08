from datetime import datetime
from flask import request, jsonify, Blueprint
from pymongo import MongoClient
from bson import ObjectId


client = MongoClient('mongodb+srv://sparta:k1716k@sparta.cwrvz74.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

update = Blueprint('update', __name__)

@update.route('/update', methods=['POST'])
def update_memo():
    memo_id = request.form['memo_id']
    content = request.form['content']
    print(" : " + memo_id)
    if not memo_id:
        return jsonify({'msg': '메모 ID가 필요합니다.'}), 400

    memo = db.memo.find_one({'_id': ObjectId(memo_id)})
    future_memo = db.futurememo.find_one({'_id': ObjectId(memo_id)})

    if memo:
        collection = db.memo
    elif future_memo:
        collection = db.futurememo
    else:
        return jsonify({'msg': '해당 메모를 찾을 수 없습니다.'}), 404

    updated_values = {}

    if content:
        updated_values['content'] = content

    updated_values['update_day'] = datetime.now()

    collection.update_one({'_id': ObjectId(memo_id)}, {'$set': updated_values})

    return jsonify({'msg': '메모가 업데이트되었습니다.'}), 200