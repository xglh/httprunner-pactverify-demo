# coding:utf-8

from flask import Flask, request, make_response

import json

app = Flask(__name__)


@app.route('/api/v1/auth', methods=['GET'])
def auth():
    rsp_body = {
        "msg": "success",
        "code": 0,
        "data": {
            "token": "c2970b75c6279b0b"
        }
    }

    rsp = make_response(json.dumps(rsp_body), 200)
    return rsp


@app.route('/api/v1/game_info', methods=['GET'])
def game_info():
    rsp_body = {
        "msg": "success",
        "code": 0,
        "data": [{
            "type_id": 249,
            "name": "王者荣耀",
            "order_index": 1,
            "status": 1,
            "subtitle": " ",
            "game_name": "王者荣耀"
        }, {
            "type_id": 250,
            "name": "绝地求生",
            "order_index": 2,
            "status": 1,
            "subtitle": " ",
            "game_name": "绝地求生"
        }
        ]
    }
    rsp = make_response(json.dumps(rsp_body), 200)
    return rsp


@app.route('/api/v1/update_game_info', methods=['POST'])
def update_game_info():
    req_body = json.loads(request.data)

    rsp_body = {
        "msg": "success",
        "code": 0,
        "data": {**req_body}
    }
    rsp = make_response(json.dumps(rsp_body), 200)
    return rsp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
