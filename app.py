import streamlit as st
from Python_project  import PJ 
from dataset import DS
from streamlit_option_menu import option_menu

def main():
    st.set_page_config(page_title='Data Analysis Dashboard',page_icon=":bar_chart:", layout='wide')

    menu = ['Page 1', 'Page 2']
    choice = st.sidebar.selectbox('Select a page', menu)

    if choice == 'Page 1':
        DS()
    elif choice == 'Page 2':
        PJ()


if __name__ == '__main__':
    main()