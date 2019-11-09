def get_veggie_response():
    return {'id': 1, 'name': ['fa', 'carrot']}

def get_vegan_response():
    return {'id': 2, 'name': ['fa', 'seedling']}

def get_gluten_response():
    return {'id': 3, 'name': ['fa', 'bread-slice']}

def get_shrimp_response():
    return {'id': 4, 'name': ['fa', 'fish']}

def get_milk_response():
    return {'id': 5, 'name': ['fa', 'blender']}

def get_ilove():
    return [get_veggie_response(), get_vegan_response()]

def get_ihate():
    return [get_veggie_response(), get_vegan_response()]

def get_icant():
    return [get_gluten_response(), get_shrimp_response(), get_milk_response()]

