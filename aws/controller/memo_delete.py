from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from bson import ObjectId


# MongoDB 연결
client = MongoClient('mongodb+srv://sparta:k1716k@sparta.cwrvz74.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# 'delete' 블루프린트 생성
delete = Blueprint('delete', __name__)

# 메모 삭제 엔드포인트
@delete.route('/delete', methods=['POST'])
def delete_memo():
    memo_id = request.form['memo_id']

    if not memo_id:
        return jsonify({'msg': '메모 ID가 필요합니다.'}), 400

    memo = db.memo.find_one({'_id': ObjectId(memo_id)})
    future_memo = db.futurememo.find_one({'_id': ObjectId(memo_id)})

    if memo:
        db.memo.delete_one({'_id': ObjectId(memo_id)})
    elif future_memo:
        db.futurememo.delete_one({'_id': ObjectId(memo_id)})
    else :
        return jsonify({'msg': '메모가 존재하지 않습니다.'}), 404

    return jsonify({'msg': '메모가 삭제되었습니다.'}), 200