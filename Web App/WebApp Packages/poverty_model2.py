import pandas as pd
import numpy as np 
from tensorflow.keras.models import load_model
import pickle
model=load_model('shortfall_predictor.h5')
with open('country_encoder.pkl','rb') as file:
    country_encoder=pickle.load(file)


def predict_total_shortfall(country, year, headcount,model,country_encoder):
    country_code=country_encoder.transform([country])
    country_code = np.array([country_code]).reshape(-1, 1)
    year = np.array([year]).reshape(-1, 1)
    headcount = np.array([headcount]).reshape(-1, 1)
    
    prediction = model.predict([country_code, year, headcount])
    
    return prediction[0][0]
