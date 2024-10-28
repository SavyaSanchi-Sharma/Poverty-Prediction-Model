import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px 

## Correlation Matrix
def plot_correlation(df):
    """
    Plots a correlation heatmap using Plotly and displays it in Streamlit.
    """
    # Select numerical columns and remove the 'year' column
    imp_col = df.select_dtypes(include=[np.number]).drop('year', axis=1)

    # Calculate the correlation matrix
    correlation = imp_col.corr()

    # Create a Plotly heatmap
    fig = px.imshow(
        correlation,
        text_auto=True,  # Annotate cells with correlation values
        color_continuous_scale='RdBu_r',  # Red-Blue color scale, reversed
        title="Correlation Matrix",
        aspect="auto",
        labels=dict(color="Correlation")
    )

    # Update layout to adjust the title and axis
    fig.update_layout(
        title_x=0.5,  # Center the title
        width=600,
        height=600
    )

    # Display the heatmap in Streamlit
    st.plotly_chart(fig)


## Graphs for Poverty_model_1

def plot_international_poverty_gap_vs_hc_ratio(filtered_data):
    """
    Plots International Poverty Gap vs. HC Ratio using a scatter plot in Altair.
    """
    st.subheader('International Poverty Gap vs. HC Ratio')

    # Create the Altair scatter plot
    scatter_chart = alt.Chart(filtered_data).mark_circle(size=60, color='royalblue').encode(
        x='hc_ratio',
        y='international_poverty_gap',
        tooltip=['hc_ratio', 'international_poverty_gap']
    ).properties(
        width=700,
        height=400
    ).interactive()  # Enables zooming and panning

    st.altair_chart(scatter_chart)

def plot_poverty_gap_vs_hc_ratio(filtered_data):
    """
    Plots $1 Poverty Gap vs. HC Ratio using a scatter plot in Altair.
    """
    st.subheader('$1 Poverty Gap vs. HC Ratio')

    # Create the Altair scatter plot
    scatter_chart = alt.Chart(filtered_data).mark_circle(size=60, color='orange').encode(
        x='hc_ratio',
        y='$1_poverty_gap',
        tooltip=['hc_ratio', '$1_poverty_gap']
    ).properties(
        width=700,
        height=400
    ).interactive()  # Enables zooming and panning

    st.altair_chart(scatter_chart)


def plot_hc_ratio_over_time(country_data, country):
    """
    Plots the HC Ratio over time for a specific country using Streamlit's line_chart.
    """
    st.subheader(f'HC Ratio Over Time for {country}')
    st.line_chart(country_data[['year', 'hc_ratio']].set_index('year'))


def plot_international_poverty_gap_over_time(country_data, country):
    """
    Plots the International Poverty Gap over time for a specific country using Streamlit's line_chart.
    """
    st.subheader(f'International Poverty Gap Over Time for {country}')
    st.line_chart(country_data[['year', 'international_poverty_gap']].set_index('year'))



def plot_poverty_gap_over_time(country_data, country):
    """
    Plots the $1 Poverty Gap over time for a specific country using Streamlit's line_chart.
    """
    st.subheader(f'$1 Poverty Gap Over Time for {country}')
    st.line_chart(country_data[['year', '$1_poverty_gap']].set_index('year'))
    
    
## Graphs for Poverty_model_2

def plot_headcount_vs_shortfall(Poverty_2):
    """
    Plots a scatter plot for headcount_international_povline vs. total_shortfall_international_povline using Streamlit's Altair chart.
    """
    st.subheader('Headcount vs. Total Shortfall (International Poverty Line)')

    # Create Altair scatter plot
    scatter_chart = alt.Chart(Poverty_2).mark_circle(size=60, color='blue').encode(
        x='headcount_international_povline',
        y='total_shortfall_international_povline',
        tooltip=['headcount_international_povline', 'total_shortfall_international_povline']
    ).properties(
        width=600,
        height=600
    ).interactive()  # Enables zooming and panning
    st.altair_chart(scatter_chart)
    
def plot_hc_ratio_over_time(df, country):
    """
    Plots HC Ratio over time for a specific country using Altair scatter plot.
    """
    st.subheader(f'HC Ratio Over Time for {country}')

    # Filter data for the selected country
    country_data = df[df['country'] == country]

    # Create Altair line chart
    line_chart = alt.Chart(country_data).mark_line(point=True).encode(
        x='year:O',  # 'year' treated as an ordinal value for better readability
        y='headcount_international_povline',
        tooltip=['year', 'headcount_international_povline']
    ).properties(
        width=700,
        height=400
    ).interactive()  # Enable zoom and pan

    # Display the chart
    st.altair_chart(line_chart)

def plot_total_shortfall_over_time(df, country):
    """
    Plots total shortfall over time for a specific country using Altair line chart.
    """
    st.subheader(f'Total Shortfall Over Time for {country}')

    # Filter data for the selected country
    country_data = df[df['country'] == country]

    # Create Altair line chart
    line_chart = alt.Chart(country_data).mark_line(point=True).encode(
        x='year:O',  # 'year' treated as an ordinal value for better readability
        y='total_shortfall_international_povline',
        tooltip=['year', 'total_shortfall_international_povline']
    ).properties(
        width=700,
        height=400
    ).interactive()  # Enable zoom and pan

    # Display the chart
    st.altair_chart(line_chart)