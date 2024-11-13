import pandas as pd
import numpy as np 
from tensorflow import keras
from keras.models import load_model
import pickle

model = load_model('poverty_predictor.h5')

with open('country_encoder.pkl', 'rb') as file:
    country_encoder = pickle.load(file)

def predict_poverty(country, year, hc_ratio,model,country_encoder):
    country_code=country_encoder.transform([country])
    country_code = np.array([country_code]).reshape(-1, 1)
    year = np.array([year]).reshape(-1, 1)
    hc_ratio = np.array([hc_ratio]).reshape(-1, 1)
    
    # Make predictions using the model
    prediction = model.predict([country_code, year, hc_ratio])
    
    return prediction[0][0],prediction[0][1]  # Return the predicted value