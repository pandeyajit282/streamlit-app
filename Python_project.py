import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In page1.py
def PJ():
    #### importing and processing the dataset 
    # import the dataset
    df = pd.read_csv("gapminder-FiveYearData.csv")

    # Sort the dataset by the continent column
    df_sorted = df.sort_values(['continent','country'], ascending=[True,True] )


    # get the data for the year 2007
    df2 = df[df["year"]== 2007]
    df2 = df2.drop('year', axis =1)

    # reset the index column
    df2.reset_index(inplace=True)

    # drop the index column
    df2.drop('index', axis = 1, inplace=True)

    # standardize the continuous in the dataset
    object = StandardScaler()
    a = object.fit_transform(df2.loc[:,['pop','gdpPercap','lifeExp']])
    df_2 = pd.DataFrame(a,columns=['pop_std','gdp_std','lifeExp_std'])


    # set the title
    st.title(":bar_chart: Data Analysis Dashboard")
     
    # new dataframe with standardize values
    df3 = pd.concat([df2, df_2],axis = 1 )
    df3.drop(["pop","lifeExp","gdpPercap"], axis =1, inplace = True)


    #### plots
    # plot 1
    ax = px.histogram(df2, x = 'continent',color="continent",title="Country count in continents")

    # plot 2
    df_af = df2[df2["continent"]== "Africa"] 
    fig1 = px.pie(df_af, values = "pop",names='country',height=600 , title = "Population of Africa continent")

    # plot 3
    df_as = df2[df2['continent']== "Asia"]
    fig2 = px.pie(df_as, values = "pop",names='country',height=600, title = "Population of Asia continent")

    # plot 4
    df_oc = df2[df2['continent']== "Oceania"] 
    fig3 = px.pie(df_oc, values = "pop",names='country',height=600, title = "Population of Oceania continent")                

    # plot 5 
    df_e = df2[df2['continent']== "Europe"] # Represent only large countries
    fig4 = px.pie(df_e, values = "pop",names='country',height=600, title = "Population of Europe continent")
                                    
    # plot 6
    df_am = df2[df2['continent']== "Americas"] 
    fig5 = px.pie(df_am, values = "pop",names='country',height=600, title = "Population of Americas continent")

    # create menu bar
    select_options = option_menu(
        menu_title=None,
        options = ["Univariate Analysis","Bivariate Analysis","Multivariate Analysis"],
        orientation="horizontal",
    )
    if select_options == "Univariate Analysis":
        with st.container():
            col1, col2 = st.columns(2)
            with col1:       
                st.plotly_chart(ax, height=50,width =50, use_container_width=True)

            with col2:
                options1 =df["continent"].unique()
                select1 = st.selectbox(
                    "Select the continent",
                    options = options1,
                )
                if select1 == "Africa":
                    # pie plot of population of Africa continent
                    st.plotly_chart(fig1,  height=700,width =500,use_container_width=True)
                if select1 == "Asia":
                    # pie plot of population of Asia continent
                    st.plotly_chart(fig2, height=700,width =500,use_container_width=True)
                if select1 == "Oceania":
                    # pie plot of population of Oceania continent
                    st.plotly_chart(fig3, height=700,width =500,use_container_width=True)
                if select1 == "Europe":
                    # pie plot of population of Europe continent
                    st.plotly_chart(fig4, height=700,width =500,use_container_width=True)
                if select1 == "Americas":
                    # pie plot of population of Americas continent
                    st.plotly_chart(fig5, height=700,width =500,use_container_width=True)        
                    
    if select_options == "Multivariate Analysis":
        # correlation matrix
        st.subheader("Correlation coeficient matrix")
        

        corr = df2.iloc[:,[1,3,4]].corr()
        fig = px.imshow(corr)
        st.plotly_chart(fig, length = 500,width= 500)



    if select_options == "Bivariate Analysis":
        # get total gdp for each country
        df["gdp"]=df["gdpPercap"]*df["pop"]         
        df

        select_options1 = st.selectbox("Please select a plot",
            options=["pop vs life_Exp","gdp vs life_Exp","gdp vs pop" ]
        )
        if select_options1 == "pop vs life_Exp":
            #  
            fig2 = px.scatter(data_frame= df,
                    x="pop",
                    y="lifeExp",
                    animation_frame="year",
                    animation_group="country", 
                    color="continent", 
                    hover_name="country",
                    log_x=True,log_y=True, size_max=55,
                    hover_data=["gdp"] 
                    )
            st.plotly_chart(fig2)

        if select_options1== "gdp vs life_Exp":
            #
            fig3 = px.scatter(data_frame= df,
                        x= "gdp",
                        y="lifeExp",
                        animation_frame="year",
                        animation_group="country",
                        color="continent", 
                        hover_name="country",
                        log_x=True,log_y=True, size_max=110, range_x=[5.2e+7,1.3e+13], range_y=[25,100],
                        hover_data=["gdpPercap"]
                        )
            st.plotly_chart(fig3)

        if select_options1 == "gdp vs pop":
            #
            fig4 = px.scatter(data_frame= df,
                    x= "gdp",
                    y="pop",
                    animation_frame="year",
                    animation_group="country",
                    color="continent", 
                    hover_name="country",
                    log_x=True,log_y=True, size_max=110,
                    hover_data=["gdpPercap"]
                    )
            st.plotly_chart(fig4)


        select_options2 = st.selectbox(
            "Boxplots",
            options=["Boxplot of gde_per_cap grouped by continent",
            "Boxplot of life_exp grouped by cpntinent"]
        )
        if select_options2 == "Boxplot of gde_per_cap grouped by continent":
            # boxplot of (continent and GDP)
            fig = px.box(df2, x="continent", y="gdpPercap")
            st.plotly_chart(fig)

        if select_options2 == "Boxplot of life_exp grouped by cpntinent":
            # boxplot of (continent and Life expectancy)
            fig = px.box(df2, x="continent", y="lifeExp")
            st.plotly_chart(fig)
            

        # data of India
        df3 = df[df["country"]=="India"]
        # data of China
        df4 = df[df["country"]=="China"]
        
        with st.container():

            col1, col2 = st.columns(2)
            with col1:
                #### Pop (India vs china)
                # Define data for first line chart
                x1 = df3["year"]
                y1 = df3["pop"]
                # Define data for second line chart
                x2 = df4["year"]
                y2 = df4["pop"]
                # Define layout for both line charts
                layout = go.Layout(title='Comparison of India and China Population Growth',
                                xaxis=dict(title='year'),yaxis=dict(title='population'))
                # Create first line chart trace
                trace1 = go.Scatter(x=x1, y=y1, mode='lines', name='Line 1', line=dict(color='blue'))
                # Create second line chart trace
                trace2 = go.Scatter(x=x2, y=y2, mode='lines', name='Line 2', line=dict(color='red'))
                # Create subplots with two line charts
                fig = make_subplots(rows=1, cols=1, shared_xaxes=True, shared_yaxes=False)
                # Add traces to subplots
                fig.add_trace(trace1, row=1, col=1)
                fig.add_trace(trace2, row=1, col=1)
                # Update layout for subplots
                fig.update_layout(layout)
                # Show plot
                st.plotly_chart(fig,length = 500, width=500,use_container_width=True)

            with col2:
                #### gdp per capita (India vs China)
                # Define data for first line chart
                x1 = df3["year"]
                y1 = df3["gdpPercap"]

                # Define data for second line chart
                x2 = df4["year"]
                y2 = df4["gdpPercap"]
                # Define layout for both line charts
                layout = go.Layout(title='Comparison of India and China GDP per capita Growth',
                                xaxis=dict(title='year'),yaxis=dict(title='gdpPercap'))
                # Create first line chart trace
                trace1 = go.Scatter(x=x1, y=y1, mode='lines', name='Line 1', line=dict(color='blue'))

                # Create second line chart trace
                trace2 = go.Scatter(x=x2, y=y2, mode='lines', name='Line 2', line=dict(color='red'))
                # Create subplots with two line charts
                fig = make_subplots(rows=1, cols=1, shared_xaxes=True, shared_yaxes=False)
                # Add traces to subplots
                fig.add_trace(trace1, row=1, col=1)
                fig.add_trace(trace2, row=1, col=1)
                # Update layout for subplots
                fig.update_layout(layout)
                # Show plot
                st.plotly_chart(fig,length = 500, width=500,use_container_width=True)

    # hide the streamlit icons
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)




