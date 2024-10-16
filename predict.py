import streamlit as st
import numpy as np


# job lib
def loadModel():
    import joblib
    with open('model.pkl', 'rb') as file:
        data = joblib.load(file)
    return data

def load_model():
    import pickle
    with open("1.pkl", "rb") as file:
        data = pickle.load(file)
    return data

data = loadModel()
classifier = data["model"]



def show_predict_page():
    st.title("Maternity Health Detection")
    st.write("Enter the following details to detect the health outcome:")

    age = st.text_input("Enter the age: ")
    
    # Systolic Blood Pressure slider (mmHg)
    systolic_bp = st.slider(
        "Systolic Blood Pressure (mmHg):",
        min_value=90, max_value=180, value=120, step=1
    )

    # Diastolic Blood Pressure slider (mmHg)
    diastolic_bp = st.slider(
        "Diastolic Blood Pressure (mmHg):",
        min_value=60, max_value=120, value=80, step=1
    )

    # Blood Sugar slider (mmol/L)
    bs = st.slider(
        "Blood Sugar (mmol/L):",
        min_value=3.0, max_value=20.0, value=5.5, step=0.1
    )

    # Body Temperature slider (Celsius)
    body_temp = st.slider(
        "Body Temperature (°C):",
        min_value=35.0, max_value=42.0, value=37.0, step=0.01
    )

    
            
    heart_rate = st.slider(
        "Heart Rate (bpm):",
        min_value=30, max_value=200, value=60, step=1
    )

    
    if st.button("Get Result"):
        # Check if all fields are filled and valid
        if age and systolic_bp and diastolic_bp and bs and body_temp and heart_rate:
            try:
                X = np.array([[float(age), float(systolic_bp), float(diastolic_bp), float(bs), float(body_temp), float(heart_rate)]])
                y = classifier.predict(X)
                st.subheader("Result")
                st.write(f"**Patients Result:** {y[0]}")
                st.write("This result is based on the data entered, including your age, blood pressure, blood sugar level, body temperature, and heart rate. Please remember that this is a predictive model and should be used for informational purposes only. For a comprehensive health assessment, consult with a healthcare professional.")
            except ValueError:
                st.error("Please enter valid numbers for all fields.")
        else:
            st.warning("Please fill in all fields.")
