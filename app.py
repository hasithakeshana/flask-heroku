from flask import Flask
from flask_restful import Api,Resource
import pickle
import pandas as pd 
from fbprophet import Prophet


app = Flask(__name__)


@app.route('/')
def main():
    return ''


@app.route('/getPrice')
def getPrice():
         # pickle file name
        file_name = 'prophet_pickle_model'

        # load the pickle file 
        loaded_model = pickle.load(open(file_name,'rb'))

        # hardcoded input of the user
        future_date = pd.DataFrame({'ds':['2018-04-01']})

        # forecast using the model
        out = loaded_model.predict(future_date)

        # print the output
        print("%.2f" % out.yhat[0])

        return {"data": round(out.yhat[0],2)}




if __name__ == '__main__':
        app.run(debug=True)



