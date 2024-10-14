import streamlit as st

def show_home():
    st.title("Welcome to Maternity Health Predictor")
    st.write("""
        This application predicts the health outcomes based on several factors like age, blood pressure, body temperature, etc.
        Use the navigation menu to explore the app.
    """)
    
    st.subheader("About")
    st.write("""
        This app is designed to assist in predicting maternity health outcomes using machine learning.
        It uses a Random Forest Classifier trained on relevant health data.
    """)
    st.subheader("Data")
    st.write("""
        The data used for training the model includes features such as:
        - Age
        - Systolic Blood Pressure
        - Diastolic Blood Pressure
        - Blood Sugar (BS)
        - Body Temperature
        - Heart Rate
        The dataset is processed and cleaned to ensure accurate predictions.
    """)
    
    st.subheader("Model Information")
    st.write("""
        The model used in this app is a Random Forest Classifier.
        It was trained on a dataset with multiple features related to maternity health.
        Future updates may include additional model types for improved accuracy.
    """)