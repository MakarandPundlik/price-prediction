#flask entry poiny for index file
from flask import Flask,render_template 
import pandas as pd

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

if __name__=="__main__":
    app.run(debug=True)


