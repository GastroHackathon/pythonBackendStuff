
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




