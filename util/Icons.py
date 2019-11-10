def get_veggie_response(art):
    return {'id': 1, 'name': ['fa', 'carrot'], 'art': art}

def get_vegan_response(art):
    return {'id': 2, 'name': ['fa', 'seedling'], 'art': art}

def get_gluten_response(art):
    return {'id': 3, 'name': ['fa', 'bread-slice'], 'art': art}

def get_shrimp_response(art):
    return {'id': 4, 'name': ['fa', 'fish'], 'art': art}

def get_milk_response(art):
    return {'id': 5, 'name': ['fa', 'blender'], 'art': art}

def get_egg_response(art):
    return {'id': 6, 'name': ['fa', 'egg'], 'art': art}

def get_bacon_response(art):
    return {'id': 6, 'name': ['fa', 'bacon'], 'art': art}

def get_hotpepper_response(art):
    return {'id': 6, 'name': ['fa', 'pepper-hot'], 'art': art}




def get_ilove():
    return [get_veggie_response('ILove'), get_vegan_response('ILove'), get_hotpepper_response('ILove'), get_bacon_response('ILove')]

def get_ihate():
    return [get_veggie_response('IHate'), get_vegan_response('IHate'), get_hotpepper_response('IHate'), get_bacon_response('IHate')]

def get_icant():
    return [get_gluten_response('ICant'), get_shrimp_response('ICant'), get_milk_response('ICant'), get_egg_response('ICant')]

