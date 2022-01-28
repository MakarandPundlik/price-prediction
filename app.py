#flask entry poiny for index file
from flask import Flask,render_template, request 
import pandas as pd
import pickle 
import numpy as np

model = pickle.load(open('CarPricePredictorModel.pkl','rb'))#read binary 
app = Flask(__name__)

#create dataframe, read csv
cars = pd.read_csv('Cleaned Car Data.csv')


@app.route("/")
def index():
    companies = sorted(cars['company'].unique())
    models = sorted(cars['name'].unique())
    year = sorted(cars['year'].unique())
    fuel_type = sorted(cars['fuel_type'].unique())
    return render_template('index.html',companies=companies,models=models,years=year,fuel_type=fuel_type)

@app.route("/predict",methods=['post'])
def predict():
    company = request.form.get('company')
    model = request.form.get('model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kms_driven'))
    prediction = model=model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=np.array([model,company,year,kms_driven,fuel_type]).reshape(1, 5)))
    print(prediction)
    #print(model.summary())
    print(prediction)
    return company
if __name__=="__main__":
    app.run(debug=True)


