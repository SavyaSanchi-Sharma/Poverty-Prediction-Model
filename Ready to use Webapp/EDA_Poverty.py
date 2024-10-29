#!/usr/bin/env python
# coding: utf-8

# Necessary imports
from Povert_Cleaning import clean_data
import pandas as pd
import numpy as np



# Function to prepare and return Poverty_1 data
def get_poverty_1_data():
    df = clean_data('pip_dataset.csv') 
    Poverty_1=df[['country', 'year', 'hc_ratio', 'international_poverty_gap', '$1_poverty_gap']].reset_index().drop(['index'], axis=1)
    return Poverty_1

# Function to prepare and return Poverty_2 data
def get_poverty_2_data():
    df = clean_data('pip_dataset.csv')
    Poverty_2=df[['country', 'year', 'headcount_international_povline', 'total_shortfall_international_povline']].reset_index().drop(['index'], axis=1)
    return Poverty_2

