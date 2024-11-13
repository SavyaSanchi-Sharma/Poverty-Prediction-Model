import Povert_Cleaning as data
import EDA_Poverty as EDA
import poverty_model1
import poverty_model2
import graphs
from tensorflow import keras
from keras.models import load_model
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
    st.title('Poverty Predictor and Visual analysis')
    df=data.clean_data('pip_dataset.csv')
    tabs=st.tabs(["Poverty Gaps Prediction and Visual Analysis","International Poverty Shortfall Prediction and Visual Analysis","About The Project","About The Dataset"])
    countries=df['country'].drop_duplicates()
    with tabs[0]: 
         st.title('Predictive Model for Global and Extreme Poverty Gaps')
         Poverty_1=EDA.get_poverty_1_data()

         country_in = st.selectbox('Select a Country:', countries, key='model_1_c')
         hc_ratio_in = st.number_input('Enter Head Count Ratio (HC Ratio):', min_value=0.0, max_value=100.0, step=0.01)
         year_in= st.number_input('Enter Year:', min_value=1967, max_value=2040, step=1,key='model_1_y')

         # prediction of international poverty gap and $1 poverty gap   
         ipg,dpg=poverty_model1.predict_poverty(country_in,year_in,hc_ratio_in,model_1,country_encoder)
         if st.button('Submit',key='model_1_b'):
             # Display the inputs
             st.write(f'In {year_in}, the average poverty gap for individuals earning below the $1 poverty threshold in {country_in} is {dpg:.3f}%')
             st.write(f'In {year_in}, the poverty gap for individuals living below the international poverty line in {country_in} is {ipg:.3f}%')
        
         st.title('Visual Analysis')
         # plotting graphs for the first model
         graphs.plot_international_poverty_gap_vs_hc_ratio(df)
         graphs.plot_poverty_gap_vs_hc_ratio(df)
         country = st.selectbox('Select a Country for Poverty Analysis:', countries,key='model_1')
         graphs.plot_hc_ratio_over_time(df,country)
         graphs.plot_international_poverty_gap_over_time(df,country)
         graphs.plot_poverty_gap_over_time(df,country)
    
    with tabs[1]:
         st.title('Forecasting International Poverty Shortfall')
         Poverty_2=EDA.get_poverty_2_data()

         country_in = st.selectbox('Select a Country:', countries, key='model_2_c')
         headcount_in = st.number_input('Enter HeadCount:', min_value=60, max_value=10**9, step=10)
         year_in= st.number_input('Enter Year:', min_value=1967, max_value=2040, step=1,key='model_2_y')

         # prediction of international poverty gap and $1 poverty gap   
         shortfall=poverty_model2.predict_total_shortfall(country_in,year_in,headcount_in,model_2,country_encoder)
         if st.button('Submit'):
             st.write(f'In {year_in}, {country_in} would need a total of ${shortfall:.3f} to eliminate poverty, based on the international poverty line.')
         st.title('Visual Analysis')
         graphs.plot_headcount_vs_shortfall(Poverty_2)
         country = st.selectbox('Select a Country for Poverty Analysis:', countries,key='model_2')
         graphs.plot_headcount_over_time(df, country)
         graphs.plot_total_shortfall_over_time(df, country)
    with tabs[2]:
        st.title('Project Overview')
        html_p='''
                 <html lang="en">
                        <head>
                          <meta charset="UTF-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1.0">
                          <title>Predicting Future Poverty Gaps and International Poverty Line Shortfall</title>
                          <style>
                            body {
                              font-family: Arial, sans-serif;
                              margin: 0;
                              padding: 0;
                              background-color: #f7f7f7;
                            }
                            .container {
                              max-width: 800px;
                              margin: 0 auto;
                              padding: 40px 20px;
                            }
                            h1 {
                              font-size: 36px;
                              font-weight: bold;
                              margin-bottom: 30px;
                            }
                            p {
                              font-size: 18px;
                              line-height: 1.6;
                              margin-bottom: 20px;
                            }
                            ul {
                              font-size: 18px;
                              line-height: 1.6;
                              margin-bottom: 20px;
                              list-style-type: disc;
                              margin-left: 20px;
                            }
                          </style>
                        </head>
                        <body>
                          <div class="container">
                            <h1>Predicting Future Poverty Gaps and International Poverty Line Shortfall</h1>
                            <p>Poverty is a persistent and multidimensional challenge faced by many countries around the world. Understanding and forecasting the dynamics of poverty is crucial for policymakers and development organizations to allocate resources effectively and design targeted interventions. One aspect of this challenge is the ability to predict future poverty gaps and the international poverty line shortfall for a specific country.</p>

                            <p>The poverty gap is the average shortfall of the total population from the poverty line. It provides a measure of the depth of poverty, indicating how far, on average, the poor are from the poverty line. The international poverty line shortfall, on the other hand, represents the amount of resources needed to lift all individuals living below the international poverty line (currently set at $2.15 per day in 2017 purchasing power parity) up to that line.</p>

                            <p>Accurately forecasting these metrics is crucial for understanding the scale of the challenge and planning appropriate policy responses. By predicting future poverty gaps and international poverty line shortfall, policymakers can:</p>

                            <ul>
                              <li>Anticipate the resource requirements needed to address poverty and allocate funding accordingly.</li>
                              <li>Identify the populations most at risk of falling into or remaining in poverty, allowing for targeted interventions.</li>
                              <li>Monitor the progress and effectiveness of existing poverty alleviation programs and make necessary adjustments.</li>
                              <li>Inform long-term development strategies and track progress towards global goals, such as the UN Sustainable Development Goals.</li>
                            </ul>

                            <p>To achieve this, I aim to develop a model that can predict the future poverty gaps and international poverty line shortfall for a particular country, based on historical data on poverty headcount and headcount ratio. This approach leverages the availability of these commonly reported poverty metrics to provide insights into the deeper dimensions of poverty.</p>
                            <p>By predicting these key indicators, I can contribute to a more comprehensive understanding of poverty dynamics and help policymakers and development organizations make informed decisions to combat poverty more effectively.</p>
                            <p>In addition, I’ve added graphs for further analysis, which can enhance the visual understanding of these metrics. The predictive models are based on Artificial Neural Networks, which allows for more accurate forecasts and great results. The ability to forecast future poverty gaps and international poverty line shortfall can be a valuable tool in the ongoing efforts to reduce poverty and improve the lives of those in need.</p>
                          </div>
                        </body>
                        </html>
        '''
        st.html(html_p)
    with tabs[3]:     
        st.title('About The Dataset')
        df_codebook=pd.read_csv('pip_codebook.csv')
        st.dataframe(df_codebook)
        st.subheader('Correlation matrix between some columns of the dataset')
        graphs.plot_correlation(df)
        st.title('More About The Dataset')
        html_d='''
                        <html>
                        <body>
                        <h2>Where is this data sourced from?</h2>
                        <p>This data explorer is collated and adapted from the World Bank's Poverty and Inequality Platform (PIP).</p>
                        <p>The World Bank's PIP data is a large collection of household surveys where steps have been taken by the World Bank to harmonize definitions and methods across countries and over time.</p>
                        <h3>About the comparability of household surveys</h3>
                        <p>There is no global survey of incomes. To understand how incomes across the world compare, researchers need to rely on available national surveys.</p>
                        <p>Such surveys are partly designed with cross-country comparability in mind, but because the surveys reflect the circumstances and priorities of individual countries at the time of the survey, there are some important differences.</p>
                        <h4>Income vs expenditure surveys</h4>
                        <p>One important issue is that the survey data included within the PIP database tends to measure people's income in high-income countries, and people's consumption expenditure in poorer countries.</p>
                        <p>The two concepts are closely related: a household's income equals their consumption plus any saving, or minus any borrowing or spending out of savings.</p>
                        <p>One important difference is that, while zero consumption is not a feasible value – people with zero consumption would starve – a zero income is a possible value. This means that, at the bottom end of the distribution, income and consumption can give quite different pictures of a person's welfare. For instance, a person dissaving in retirement may have a very low, or even zero, income, but have a high level of consumption nevertheless.</p>
                        <p>The gap between income and consumption is higher at the top of this distribution too, richer households tend to save more, meaning that the gap between income and consumption is higher at the top of this distribution too. Taken together, one implication is that inequality measured in terms of consumption is generally somewhat lower than the inequality measured in terms of income.</p>
                        <p>In our Data Explorer of this data, there is the option to view only income survey data or only consumption survey data, or instead to pool the data available from both types of survey – which yields greater coverage.</p>
                        <h4>Other comparability issues</h4>
                        <p>There are a number of other ways in which comparability across surveys can be limited. The PIP Methodology Handbook provides a good summary of the comparability and data quality issues affecting this data and how it tries to address them.</p>
                        <p>In collating this survey data the World Bank takes a range of steps to harmonize it where possible, but comparability issues remain. These affect comparisons both across countries and within individual countries over time.</p>
                        <p>To help communicate the latter, the World Bank produces a variable that groups surveys within each individual country into more comparable 'spells'. Our Data Explorer provides the option of viewing the data with these breaks in comparability indicated, and these spells are also indicated in our data download.</p>
                        <h3>Global and regional poverty estimates</h3>
                        <p>Along with data for individual countries, the World Bank also provides global and regional poverty estimates which aggregate over the available country data.</p>
                        <p>Surveys are not conducted annually in every country however – coverage is generally poorer the further back in time you look and remains particularly patchy within Sub-Saharan Africa. You can see that visualized in our chart of the number of surveys included in the World Bank data by decade.</p>
                        <p>In order to produce global and regional aggregate estimates for a given year, the World Bank takes the surveys falling closest to that year for each country and 'lines up' the data to the year being estimated by projecting it forward or backward.</p>
                        <p>This lining-up is generally done on the assumption that household incomes or expenditure grow in line with the growth rates observed in national accounts data. You can read more about the interpolation methods used by the World Bank in Chapter 5 of the Poverty and Inequality Platform Methodology Handbook.</p>
                        <h3>How does the data account for inflation and for differences in the cost of living across countries?</h3>
                        <p>To account for inflation and price differences across countries, the World Bank's data is measured in international dollars. This is a hypothetical currency that results from price adjustments across time and place. It is defined as having the same purchasing power as one US-$ would in the United States in a given base year. One int.-$ buys the same quantity of goods and services no matter where or when it is spent.</p>
                        <p>There are many challenges to making such adjustments and they are far from perfect. Angus Deaton (Deaton, 2010) provides a good discussion of the difficulties involved in price adjustments and how this relates to global poverty measurement.</p>
                        <p>But in a world where price differences across countries and over time are large, it is important to attempt to account for these differences as well as possible, and this is what these adjustments do.</p>
                        <p>In September 2022, the World Bank updated its methodology, and now uses international-$ expressed in 2017 prices – updated from 2011 prices. This has had little effect on our overall understanding of poverty and inequality around the world. But poverty estimates for particular countries vary somewhat between the old and updated methodology. You can read more about this update in our article From $1.90 to $2.15 a day: the updated International Poverty Line.</p>
                        <p>To allow for comparisons with the official data now expressed in 2017 international-$ data, the World Bank continues to release its poverty and inequality data expressed in 2011 international-$ as well. We have built a Data Explorer to allow you to compare these, and we make all figures available in terms of both sets of prices in our data download.</p>
                        <h3>Absolute vs relative poverty lines</h3>
                        <p>This dataset provides poverty estimates for a range of absolute and relative poverty lines.</p>
                        <p>An absolute poverty line represents a fixed standard of living; a threshold that is held constant across time. Within the World Bank's poverty data, absolute poverty lines also aim to represent a standard of living that is fixed across countries (by converting local currencies to international-$). The International Poverty Line of 2.15 per day (in 2017 international-$) is the best-known absolute poverty line and is used by the World Bank and the UN to measure extreme poverty around the world.</p>
                        <p>The value of relative poverty lines instead rises and falls as average incomes change within a given country. In most cases, they are set at a certain fraction of the median income. Because of this, relative poverty can be considered a metric of inequality – it measures how spread out the bottom half of the income distribution is.</p>
                        <p>The idea behind measuring poverty in relative terms is that a person's well-being depends not on their own absolute standard of living but on how that standard compares with some reference group, or whether it enables them to participate in the norms and customs of their society. For instance, joining a friend's birthday celebration without shame might require more resources in a rich society if the norm is to go for an expensive meal out, or give costly presents.</p>
                        <p>Our dataset includes three commonly-used relative poverty lines: 40%, 50%, and 60% of the median.</p>
                        <p>Such lines are most commonly used in rich countries, and are the main way poverty is measured by the OECD and the European Union.</p>
                        <p>More recently, relative poverty measures have come to be applied in a global context. The share of people living below 50% of the median income is, for instance, one of the UN's Sustainable Development Goal indicators. And the World Bank now produces estimates of global poverty using a Societal Poverty Line that combines absolute and relative components.</p>
                        <p>When comparing relative poverty rates around the world, however, it is important to keep in mind that – since average incomes are so far apart – such relative poverty lines relate to very different standards of living in rich and poor countries.</p>
                        <h3>Does the data account for non-market income, such as food grown by subsistence farmers?</h3>
                        <p>Many poor people today, as in the past, rely on subsistence farming rather than a monetary income gained from selling goods or their labor on the market. To take this into account and make a fair comparison of their living standards, the statisticians that produce these figures estimate the monetary value of their home production and add it to their income/expenditure.</p>
                        </body>
                        </html>
        '''
        st.html(html_d)
if __name__=="__main__":
    main()