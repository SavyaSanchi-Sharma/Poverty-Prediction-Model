import Povert_Cleaning as data
import EDA_Poverty as EDA
import poverty_model1
import poverty_model2
import graphs
from tensorflow.keras.models import load_model
import pickle
import streamlit
import pandas as pd 
import numpy as np
import streamlit as st
import altair as alt
import plotly.express as px 

model_1 = load_model('poverty_predictor.h5')
model_2 = load_model('shortfall_predictor.h5')
with open('country_encoder.pkl','rb') as file:
    country_encoder=pickle.load(file)
    
    
def main():
    st.title('Poverty Predictor and Poverty analysis')
    df=data.clean_data('pip_dataset.csv')
    st.subheader('About The Dataset')
    graphs.plot_correlation(df)
    
    countries=df['country'].drop_duplicates()
    Poverty_1=EDA.get_poverty_1_data()
    
    country_in = st.selectbox('Select a Country:', countries)
    hc_ratio_in = st.number_input('Enter Head Count Ratio (HC Ratio):', min_value=0.0, max_value=100.0, step=0.01)
    year_in= st.number_input('Enter Year:', min_value=1967, max_value=2040, step=1)
    
    # prediction of international poverty gap and $1 poverty gap   
    ipg,dpg=poverty_model1.predict_poverty(country_in,year_in,hc_ratio_in,model_1,country_encoder)
    if st.button('Submit'):
        # Display the inputs
        st.write(f'Poverty ratio of people earning atleast $1 in {country_in} in  {year_in} is {dpg:.3f}')
        st.write(f'Poverty ratio of people earning below international poverty line in {country_in} in {year_in} is {ipg:.3f}')

    # plotting graphs for the first model
    graphs.plot_international_poverty_gap_vs_hc_ratio(df)
    graphs.plot_poverty_gap_vs_hc_ratio(df)
    country = st.selectbox('Select a Country for Poverty Analysis:', countries)
    graphs.plot_hc_ratio_over_time(df,country)
    graphs.plot_international_poverty_gap_over_time(df,country)
    graphs.plot_poverty_gap_over_time(df,country)
    
    
    
    
if __name__=="__main__":
    main()