import streamlit as st
from home import show_home
from detect import show_predict_page
from about_data import show_about_data
from model_overview import show_model_overview

# Navigation sidebar
st.sidebar.title("Menu")
page = st.sidebar.selectbox("Choose a page", ["Home","About data","Model overview","detect"])


# Render the selected page
if page == "Home":
    show_home()
elif page == "detect":
    show_predict_page()
    
elif page == "About data":
    show_about_data()
elif page == "Model overview":
    show_model_overview()
