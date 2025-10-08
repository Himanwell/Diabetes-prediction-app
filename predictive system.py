# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import pickle

# loading the saved model
loaded_model = pickle.load(open("C:/Users/Emmanuel/OneDrive/Desktop/Deployimng machine learning model/trained_model.sav", "rb"))

feature_names = ["Pregnancies","Glucose","BloodPressure","SkinThickness",
                 "Insulin","BMI","DiabetesPedigreeFunction","Age"]

input_data = (3,158,76,36,245,31.6,0.851,28)

# Put into DataFrame with column names
input_data = pd.DataFrame([input_data], columns=feature_names)


prediction = loaded_model.predict(input_data)
print(prediction)

if (prediction[0] == 0):
  print("The person is not diabetic")
else:
  print("The person is diabetic")
