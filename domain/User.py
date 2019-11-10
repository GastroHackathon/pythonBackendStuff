
import json as js
import os



class User():
    def __init__(self):
        self.name = 'ALEX'
        self.dishes = []
        self.dish_history = ['Spaghetti mit Shrimps in einer feinen Knoblauchrahmsauce',
                             'Wiener Schnitzl']

    def load_dishes(self):
        print(os.getcwd())
        if not self.dishes:
            with open('data/dishes_full.json') as f:
                dishes = js.load(f)
            self.dishes = dishes

    def filter_preferences(self, id):
        if id == 1:
            self.dishes = [dish for dish in self.dishes if not dish['veggie']]
            print(self.dishes)
        if id == 2 :
            self.dishes = [dish for dish in self.dishes if not dish['vegan']]
        if id == 3:
            self.dishes = [dish for dish in self.dishes if not 'A' in dish['allergens']]
        if id == 4:
            self.dishes = [dish for dish in self.dishes if not dish['fish']]
        if id == 5:
            self.dishes = [dish for dish in self.dishes if not 'G' in dish['allergens']]



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