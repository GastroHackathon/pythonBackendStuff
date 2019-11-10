from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask import Response

from util.Icons import get_ihate
from util.Icons import get_ilove
from util.Icons import get_icant

from util.Images import get_image_list

from util.Questions import get_first_question_response
from util.Questions import get_second_question_response
from util.Questions import get_third_question_response
from util.Questions import get_final_flag

from domain.User import User

import json as js
import os

app = Flask(__name__)
CORS(app)
dishes = []

@app.route('/profileGeneral', methods=['GET'])
def getProfileGeneral():
    art = request.args.get('art')
    if art == 'ILove':
        print(get_ilove())
        return Response(js.dumps(get_ilove()), mimetype='application/json')
    elif art == 'IHate':
        return Response(js.dumps(get_ihate()), mimetype='application/json')
    elif art == 'ICant':
        return Response(js.dumps(get_icant()), mimetype='application/json')


@app.route('/profileGeneral', methods=['POST'])
def postProfileGeneral():
    print(request.json)   
    new_user = User()
    new_user.load_dishes()
    req = js.loads(request.data)

    if req['art'] == 'ICant' :
        new_user.filter_preferences(req['id'])
    #if req['art'] == 'ICant':
    # TODO do something with the data
    return Response(js.dumps(True), mimetype='application/json')


@app.route('/profileFood', methods=['GET'])
def getProfileFood():
    return Response(js.dumps(get_image_list()), mimetype='application/json')


@app.route('/profileFood', methods=['POST'])
def postProfileFood():
    print(request.json)
    return Response(js.dumps(True), mimetype='application/json')
    # TODO do something with the data


@app.route('/question', methods=['GET'])
def question():
    cnt = request.args.get('cnt')
    if cnt == '1':
        return Response(js.dumps(get_first_question_response()), mimetype='application/json')
    elif cnt == '2':
        return Response(js.dumps(get_second_question_response()), mimetype='application/json')
    elif cnt == '3':
        return Response(js.dumps(get_third_question_response()), mimetype='application/json')
    else:
        return Response(js.dumps(get_final_flag()), mimetype='application/json')


@app.route('/results')
def results():
    return Response(js.dumps(True), mimetype='application/json') 


if __name__ == '__main__':
    app.run()

