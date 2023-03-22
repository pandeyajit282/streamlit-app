import streamlit as st 
import pandas as pd
import numpy as np


def DS():

    # dataset
    df = pd.read_csv("gapminder-FiveYearData.csv")

    # set the title
    st.title(":bar_chart: Data Analysis Dashboard")


    #### Data analysis and EDA part
    # sidebar
    st.sidebar.header("Filters")
    continent = st.sidebar.multiselect(
        "Select the continent :",
        options=df["continent"].unique(),
        default=df["continent"].unique()
    )
    year = st.sidebar.multiselect(
        "Select year:",options=df["year"].unique(),default=df["year"].unique()
    )

    st.subheader("Dataset") 
    # data frame for multiselect 
    df_selection = df.query(
        "continent == @continent & year== @year"
    )

    # upload dataframe
    st.dataframe(df_selection)

    st.subheader("Description of data:")
    st.write("It provides data about the population, life expectancy and GDP in different countries of the world from 1952 to 2007. There is also a separate file for 2007.")



    # hide the streamlit icons
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)