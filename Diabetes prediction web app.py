# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 11:58:52 2025

@author: Emmanuel
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open("C:/Users/Emmanuel/OneDrive/Desktop/Deployimng machine learning model/trained_model.sav", "rb"))

# Creating a function for prediction

def diabetes_prediction(input_data):
    feature_names = ["Pregnancies","Glucose","BloodPressure","SkinThickness",
                     "Insulin","BMI","DiabetesPedigreeFunction","Age"]


    # Put into DataFrame with column names
    input_data = pd.DataFrame([list(map(float, input_data))], columns=feature_names)


    prediction = loaded_model.predict(input_data)
    print(prediction)

    if (prediction[0] == 0):
      return"The person is not diabetic"
    else:
      return"The person is diabetic"
      
def main():
    
    # giving a title
    st.title("Diabetes Prediction Web APP")
    
    # getting the input data from the user
    
    Pregnancies = st.text_input("Number of pregnancies")
    Glucose = st.text_input("Glucose level")
    BloodPressure = st.text_input("Blood pressure value")
    SkinThickness = st.text_input("Skin Thickness value")
    Insulin = st.text_input("Insulin level")
    BMI = st.text_input("BMI value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    Age = st.text_input("Age of the person")
    
    
    # code for prediction
    diagnosis = ""
    
    # creating a button for prediction
    
    if st.button("Diabetes Test Result"):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
    
    
    
if __name__ == "__main__":
    main()
 

    
    
      
