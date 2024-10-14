import streamlit as st

def show_about_data():
    st.title("About the Data")
    st.write("""
        The data we're using in this app comes from a dataset on Kaggle, a popular platform for sharing data and projects.

        This dataset includes health information related to maternity, and it's used to predict the risk level for expecting mothers. Here are the key features:

        - **Age**: The age of the mother.
        - **Systolic BP**: The systolic blood pressure (the higher number in a blood pressure reading).
        - **Diastolic BP**: The diastolic blood pressure (the lower number in a blood pressure reading).
        - **BS**: Blood sugar levels.
        - **Body Temp**: The mother's body temperature (in Fahrenheit).
        - **Heart Rate**: The mother's heart rate.
        - **Risk Level**: The predicted risk level for the mother (e.g., high risk, low risk).

        We use this information to help predict the risk level, so healthcare providers can take better care of expecting mothers.
    """)