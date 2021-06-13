from flask import Flask,jsonify,request
from flask_restful import Api,Resource
import pickle
import pandas as pd 
from fbprophet import Prophet
import random


app = Flask(__name__)


@app.route('/')
def main():
    return ''


@app.route('/getBeansPrice', methods=['POST'])
def getPrice():


        # user inputs
        data = request.get_json();

        user_date = data.get('date', '');

         # pickle file name
        file_name = 'prophet_pickle_model'

        # load the pickle file 
        loaded_model = pickle.load(open(file_name,'rb'))

        user_input = '2018-04-10';

        # hardcoded input of the user
        future_date = pd.DataFrame({'ds':[user_date]})

        # forecast using the model
        out = loaded_model.predict(future_date)

        # print the output
        print("%.2f" % out.yhat[0])

        # n = random.randint(100,150)
        # print(n);

        # convert to jsons
        return {
        "vegetable-code" : "TY-BEANS",
        "vegetable-name" : "beans",
        "area" : "nuwaraeliya",
        "price-output": round(out.yhat[0],2),
        "status-code": 200
        }

@app.route('/getCarrotPrice', methods=['POST'])
def getCarrot():

    n = random.randint(100,200)
    print(n);

     # convert to jsons
    return {
        "vegetable-code" : "TY-Carrot",
        "vegetable-name" : "carrot",
        "area" : "nuwaraeliya",
        "price-output": n ,
        "status-code": 200
        }

@app.route('/getTomatoPrice', methods=['POST'])
def getTomato():

    n = random.randint(80,150)
    print(n);

     # convert to jsons
    return {
        "vegetable-code" : "TY-Tomato",
        "vegetable-name" : "tomato",
        "area" : "nuwaraeliya",
        "price-output": n ,
        "status-code": 200
        }        


if __name__ == '__main__':
        app.run(debug=True)



