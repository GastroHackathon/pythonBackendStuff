from flask import Flask
from flask import request
from flask import jsonify

from util.Icons import get_ihate
from util.Icons import get_ilove
from util.Icons import get_icant

from flask_cors import CORS

from util.Images import get_image_list

from util.Questions import get_first_question_response
from util.Questions import get_second_question_response
from util.Questions import get_third_question_response
from util.Questions import get_final_flag

app = Flask(__name__)
CORS(app)


@app.route('/profileGeneral', methods=['GET'])
def getProfileGeneral():
    art = request.args.get('art')
    if art == 'ILove':
        return jsonify(get_ilove())
    elif art == 'IHate':
        return jsonify(get_ihate())
    elif art == 'ICant':
        return jsonify(get_icant())


@app.route('/profileGeneralPost', methods=['POST'])
def postProfileGeneral():
    print(request.json)
    # TODO do something with the data


@app.route('/profileFood', methods=['GET'])
def getProfileFood():
    return jsonify(get_image_list())


@app.route('/profileFood', methods=['POST'])
def postProfileFood():
    print(request.json)
    # TODO do something with the data


@app.route('/question', methods=['GET'])
def question():
    cnt = request.args.get('cnt')
    if cnt == 1:
        return jsonify(get_first_question_response())
    elif cnt == 2:
        return jsonify(get_second_question_response())
    elif cnt == 3:
        return jsonify(get_third_question_response())
    elif cnt == 4:
        return jsonify(get_final_flag())


@app.route('/results')
def results():
    return None


if __name__ == '__main__':
    app.run()
