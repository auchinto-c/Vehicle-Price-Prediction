# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 17:11:21 2022

@author: Auchinto Chatterjee
"""

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('rf_model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()

@app.route('/predict', methods=['POST'])
def predict():
    Fuel_Type_Diesel = 0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price = int(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']
        Seller_Type_Individual = request.form['Seller_Type_Individual']
        Transmission_Manual = request.form['Transmission_Manual']
        
        if(Fuel_Type_Petrol == 'Petrol'):
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        elif(Fuel_Type_Petrol == 'Diesel'):
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0
            
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0
            
        if(Transmission_Manual=='Manual'):
            Transmission_Manual=1
        else:
            Transmission_Manual=0
            
        Num_Year = 2022 - Year
            
        prediction = model.predict([[Present_Price, Kms_Driven, Owner, Num_Year, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
        output = round(prediction[0], 2)
        
        if output < 0:
            return render_template('index.html', predcition_text = 'Sorry you cannot sell this car')
        else:
            return render_template('index.html', predcition_text = 'You can sell the car at {}M'.format(output))
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app,run(debug=True)