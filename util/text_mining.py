#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 22:19:35 2019

@author: drx
"""


from sklearn.feature_extraction.text import CountVectorizer


def adventure_filter(dishes, dish_history, adventurous=True):
    
    word_list = ['mit', 'an', 'auf', 'aus', 'dazu',
                 'von', 'vom', 'se', 'und','in', 'im', 'der', 'dem']
    
    count_vect = CountVectorizer(analyzer = 'word', 
                                 stop_words=word_list,
                                 lowercase=False)
    
    available_dishes = [dish['name'] for dish in dishes]
    
    count_vect.fit_transform(dish_history)
    dish_history = [word for word in count_vect.vocabulary_]
    if adventurous:
        for blocker in dish_history:
            available_dishes = [dish for dish in available_dishes if blocker not in dish]
    else:
        for blocker in dish_history:
            available_dishes = [dish for dish in available_dishes if blocker in dish]

    available_dishes = [dish for dish in dishes if dish['name'] in available_dishes]
    return available_dishes


"""
# test filter
with open('data/dishes_full.json', encoding='utf-8') as f:
    dishes = json.load(f)

dish_history = ['Großmutters Kalbsrahmbeuschl mit Semmelknödel']

new_dishes = adventure_filter(dishes, dish_history)
print(len(dishes), len(new_dishes))
    
    
    """