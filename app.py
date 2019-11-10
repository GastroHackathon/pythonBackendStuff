import json
import json as js

from flask import Flask
from flask import Response
from flask import request
from flask_cors import CORS

from domain.User import User
from util.Icons import get_icant
from util.Icons import get_ihate
from util.Icons import get_ilove
from util.Images import get_image_list
from util.Questions import get_final_flag
from util.Questions import get_first_question_response
from util.Questions import get_second_question_response
from util.Questions import get_third_question_response
from util.machine_learning import predict_choice
from util.text_mining import adventure_filter

app = Flask(__name__)
CORS(app)
dishes = []
new_user = User()
new_user.load_dishes()


@app.route('/profileGeneral', methods=['GET'])
def getProfileGeneral():
    new_user = User()
    new_user.load_dishes()

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
    req = js.loads(request.data)
    if req['art'] == 'ICant':
        new_user.filter_preferences(req['id'])

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


@app.route('/question', methods=['POST'])
def postQuestion():
    req = js.loads(request.data)

    if req['id'] == 1:
        if req['answerId'] == 0:
            new_user.filter_preferences(1)
    elif req['id'] == 2:
        if req['answerId'] == 0:
            new_user.dishes = adventure_filter(new_user.dishes, new_user.dish_history)
        else:
            new_user.dishes = adventure_filter(new_user.dishes, new_user.dish_history, False)
        print(new_user.dishes)

    return Response(js.dumps(True), mimetype='application/json')


@app.route('/results')
def results():
    res = predict_choice(new_user.dishes)
    res = [dish for dish in new_user.dishes if dish['name'] in list(res['name'])]
    output = []
    for r in res:
        if r not in output:
            output.append(r)
    with open('data/restaurants.json') as f:
        restaurants = json.load(f)
    for dish in output:
        key = list(dish['available_in'].keys())[0]
        restaurant = [restaurant for restaurant in restaurants if restaurant['place_id'] == key]
        dish['available_in']['data'] = restaurant
    return Response(js.dumps(output), mimetype='application/json')


if __name__ == '__main__':
    app.run()
