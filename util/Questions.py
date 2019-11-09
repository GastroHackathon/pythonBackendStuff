def get_first_question_response():
    return {'id': 1, 'question': 'Would you prefer omni or veggie?', 'answer': ['Meat', 'Veggie'], 'continue': True}


def get_second_question_response():
    return {'id': 2, 'question': 'Wanna try out something new?', 'answer': ['New', 'Save known choice'], 'continue': True}

def get_third_question_response():
    # TODO generate this question
    return {'id': 3, 'question': 'How about shrimp?', 'answer': ['Yes', 'No way, shrimp is disgusting'], 'continue': True}

def get_final_flag():
    return {'id': 4, 'question': '', 'answer': [''], 'continue': False}