#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:30:33 2019

@author: drx
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix  
from sklearn.neighbors import KNeighborsClassifier  
import pandas as pd
import pickle


def preprocess(dishes):
    data_mockup = pd.read_csv('data/data_mockup.csv')
    country_list = ['Austria', 'Japan', 'China', 'Italy', 'Turkey']
    data_all_dishes = pd.DataFrame()
    for dish in dishes:
        dish_data = data_mockup
        for atribute in dish_data:
            if atribute not in country_list:
                dish_data[atribute] = dish[atribute]
        dish_data[dish['origin']] = True
        data_all_dishes = data_all_dishes.append(dish_data)    
    return data_all_dishes

def predict_choice(dishes): # user
    model = pickle.load(open('data/KNeighborsClassifier_latest' , 'rb'))#+user['username']
    data_all_dishes = preprocess(dishes)
    pred_data = data_all_dishes.drop('name', axis = 1)        
    y_hat = model.predict_proba(pred_data)
    y_hat = pd.DataFrame(y_hat)
    data_all_dishes['y'] = y_hat[1]
    data_all_dishes = data_all_dishes.sort_values('y', ascending=False)
    return data_all_dishes.iloc[:3]



"""   
# creat training data
with open('data/dishes_full.json') as f:
    dishes = json.load(f)

data_all_dishes = preprocess(dishes)
data_all_dishes.shape

data_all_dishes.to_csv('data/training_data_premature.csv')
    
# train model
data_all_dishes = pd.read_csv('data/training_data.csv')
training_data = data_all_dishes.drop('Unnamed: 0', axis=1)

X = training_data.drop(['y', 'name'], axis=1)
y = training_data['y']

## get train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1 , test_size=0.2)

model = KNeighborsClassifier(n_neighbors=10)  
model.fit(X_train, y_train)


y_hat = model.predict(X_test)  
#training_data['y_hat'] = y_hat

print(confusion_matrix(y_test, y_hat))  
print(classification_report(y_test, y_hat))

model.fit(X, y)

# persistance
import os
os.getcwd()
modelname = type(model).__name__+'_latest'
pickle.dump(model, open('data/'+modelname, 'wb'))

"""