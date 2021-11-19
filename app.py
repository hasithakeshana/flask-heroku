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
        key = data.get('key', '');

        
        if key != "MuMEO0q447d3QnEOAfUP":
                print("Invalid Key ! please check the API key, Please purchase a key, If you don't have! ")
                return {"error" : "Invalid Key ! please check the API key, Please purchase a key, If you don't have!"}

        else:        

                # pickle file name
                file_name = 'prophet_pickle_model2.pkl'

                # load the pickle file
                loaded_model = pickle.load(open(file_name,'rb'))

                future_date = pd.DataFrame({'ds':[user_date]})

                # forecast using the model
                out = loaded_model.predict(future_date)

                # print the output
                print("%.2f" % out.yhat[0])

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

     # user inputs
        data = request.get_json();

        user_date = data.get('date', '');
        key = data.get('key', '');

        if key != "MuMEO0q447d3QnEOAfUP":
                print("Invalid Key ! please check the API key, Please purchase a key, If you don't have! ")
                return {"error" : "Invalid Key ! please check the API key, Please purchase a key, If you don't have!"}

        else:

                # pickle file name
                file_name = 'prophet_pickle_model2.pkl'

                # load the pickle file
                loaded_model = pickle.load(open(file_name,'rb'))

                future_date = pd.DataFrame({'ds':[user_date]})

                # forecast using the model
                out = loaded_model.predict(future_date)

                # print the output
                print("%.2f" % out.yhat[0])

                # convert to jsons
                return {
                "vegetable-code" : "TY-CARROT",
                "vegetable-name" : "carrot",
                "area" : "nuwaraeliya",
                "price-output": round(out.yhat[0],2),
                "status-code": 200
                }
    

@app.route('/getPotatoPrice', methods=['POST'])
def getPotato():

         # user inputs
        data = request.get_json();

        user_date = data.get('date', '');
        key = data.get('key', '');

        if key != "MuMEO0q447d3QnEOAfUP":
                print("Invalid Key ! please check the API key, Please purchase a key, If you don't have! ")
                return {"error" : "Invalid Key ! please check the API key, Please purchase a key, If you don't have!"}

        else:

                # pickle file name
                file_name = 'prophet_pickle_model2.pkl'

                # load the pickle file
                loaded_model = pickle.load(open(file_name,'rb'))

                future_date = pd.DataFrame({'ds':[user_date]})

                # forecast using the model
                out = loaded_model.predict(future_date)

                # print the output
                print("%.2f" % out.yhat[0])

                # convert to jsons
                return {
                "vegetable-code" : "TY-POTATO",
                "vegetable-name" : "potato",
                "area" : "nuwaraeliya",
                "price-output": round(out.yhat[0],2),
                "status-code": 200
                }

@app.route('/getTomatoPrice', methods=['POST'])
def getTomato():

         # user inputs
        data = request.get_json();

        user_date = data.get('date', '');
        key = data.get('key', '');

        if key != "MuMEO0q447d3QnEOAfUP":
                print("Invalid Key ! please check the API key, Please purchase a key, If you don't have! ")
                return {"error" : "Invalid Key ! please check the API key, Please purchase a key, If you don't have!"}

        else:

                # pickle file name
                file_name = 'prophet_pickle_model1'

                # load the pickle file
                loaded_model = pickle.load(open(file_name,'rb'))

                future_date = pd.DataFrame({'ds':[user_date]})

                # forecast using the model
                out = loaded_model.predict(future_date)

                # print the output
                print("%.2f" % out.yhat[0])

                # convert to jsons
                return {
                "vegetable-code" : "TY-TOMATO",
                "vegetable-name" : "tomato",
                "area" : "nuwaraeliya",
                "price-output": round(out.yhat[0],2),
                "status-code": 200
                }

@app.route('/getCabbagePrice', methods=['POST'])
def getCabbage():

         # user inputs
        data = request.get_json();

        user_date = data.get('date', '');
        key = data.get('key', '');

        if key != "MuMEO0q447d3QnEOAfUP":
                print("Invalid Key ! please check the API key, Please purchase a key, If you don't have! ")
                return {"error" : "Invalid Key ! please check the API key, Please purchase a key, If you don't have!"}

        else:

                # pickle file name
                file_name = 'prophet_pickle_model1'

                # load the pickle file
                loaded_model = pickle.load(open(file_name,'rb'))

                future_date = pd.DataFrame({'ds':[user_date]})

                # forecast using the model
                out = loaded_model.predict(future_date)

                # print the output
                print("%.2f" % out.yhat[0])

                # convert to jsons
                return {
                "vegetable-code" : "TY-CABBAGE",
                "vegetable-name" : "cabbage",
                "area" : "nuwaraeliya",
                "price-output": round(out.yhat[0],2),
                "status-code": 200
                }


@app.route('/getBeetrootPrice', methods=['POST'])
def getBeetroot():

         # user inputs
        data = request.get_json();

        user_date = data.get('date', '');
        key = data.get('key', '');

        if key != "MuMEO0q447d3QnEOAfUP":
                print("Invalid Key ! please check the API key, Please purchase a key, If you don't have! ")
                return {"error" : "Invalid Key ! please check the API key, Please purchase a key, If you don't have!"}

        else:

                # pickle file name
                file_name = 'prophet_pickle_model1'

                # load the pickle file
                loaded_model = pickle.load(open(file_name,'rb'))

                future_date = pd.DataFrame({'ds':[user_date]})

                # forecast using the model
                out = loaded_model.predict(future_date)

                # print the output
                print("%.2f" % out.yhat[0])

                # convert to jsons
                return {
                "vegetable-code" : "TY-BEETROOT",
                "vegetable-name" : "beetroot",
                "area" : "nuwaraeliya",
                "price-output": round(out.yhat[0],2),
                "status-code": 200
                }



@app.route('/getBeansPriceRangeMonths', methods=['POST'])
def getBeansRangePrice():


        # user inputs
        data = request.get_json();

        start_date = data.get('startdate', '');
        end_date = data.get('enddate', '');

         # pickle file name
        file_name = 'prophet_pickle_model2.pkl'

        # load the pickle file 
        loaded_model = pickle.load(open(file_name,'rb'))

        future = pd.DataFrame({'ds': pd.date_range(start=start_date, end= end_date, freq='M')})
        
        # forecast using the model
        out = loaded_model.predict(future);

        print(out.yhat[0])

        responseData = out.yhat;

        print(responseData.to_json());

        c = responseData.to_json();


       # convert to jsons
        return {
        "vegetable-code" : "TY-BEANS",
        "vegetable-name" : "beans",
        "area" : "nuwaraeliya",
        "price-output": c,
        "status-code": 200
        }

@app.route('/getTomatoPriceRangeMonths', methods=['POST'])
def getTomatoRangePrice():


        # user inputs
        data = request.get_json();

        start_date = data.get('startdate', '');
        end_date = data.get('enddate', '');

         # pickle file name
        file_name = 'prophet_pickle_model1'

        # load the pickle file 
        loaded_model = pickle.load(open(file_name,'rb'))

        future = pd.DataFrame({'ds': pd.date_range(start=start_date, end= end_date, freq='M')})
        
        # forecast using the model
        out = loaded_model.predict(future);

        print(out.yhat[0])

        responseData = out.yhat;

        print(responseData.to_json());

        c = responseData.to_json();


       # convert to jsons
        return {
        "vegetable-code" : "TY-TOMATO",
        "vegetable-name" : "tomato",
        "area" : "nuwaraeliya",
        "price-output": c,
        "status-code": 200
        }

# prices without validations


@app.route('/BeansPrice', methods=['POST'])
def getBPrice():


        # user inputs
        data = request.get_json();

        user_date = data.get('date', '');
        
        # pickle file name
        file_name = 'prophet_pickle_model2.pkl'

        # load the pickle file
        loaded_model = pickle.load(open(file_name,'rb'))

        future_date = pd.DataFrame({'ds':[user_date]})

        # forecast using the model
        out = loaded_model.predict(future_date)

        # print the output
        print("%.2f" % out.yhat[0])

        # convert to jsons
        return {
        "vegetable-code" : "TY-BEANS",
        "vegetable-name" : "beans",
        "area" : "nuwaraeliya",
        "price-output": round(out.yhat[0],2),
        "status-code": 200
        }


@app.route('/TomatoPrice', methods=['POST'])
def getT():

         # user inputs
        data = request.get_json();

        user_date = data.get('date', '');
        
        # pickle file name
        file_name = 'prophet_pickle_model1'

        # load the pickle file
        loaded_model = pickle.load(open(file_name,'rb'))

        future_date = pd.DataFrame({'ds':[user_date]})

        # forecast using the model
        out = loaded_model.predict(future_date)

        # print the output
        print("%.2f" % out.yhat[0])

        # convert to jsons
        return {
        "vegetable-code" : "TY-TOMATO",
        "vegetable-name" : "tomato",
        "area" : "nuwaraeliya",
        "price-output": round(out.yhat[0],2),
        "status-code": 200
        }

if __name__ == '__main__':
        app.run(debug=True)



