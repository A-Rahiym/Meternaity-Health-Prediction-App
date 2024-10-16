import streamlit as st

def show_model_overview():
    st.title("Model Overview")
    st.write("""
      **Model Overview**  
In this app, we use a Maternity Health detector to evaluate various factors like age, blood pressure, and body temperature to predict health outcomes.

**Why Random Forest?**  
Random Forest emerged as the top-performing model in our evaluation. It is a powerful machine learning algorithm that builds multiple decision trees and aggregates their results for accurate health predictions. This ensemble method ensures reliable results and reduces overfitting, making it ideal for health-related predictions.

**Model Comparison**  
We evaluated several models, including:

- Logistic Regression
- Random Forest
- Gradient Boosting Classifier
- Support Vector Classifier
- K-Nearest Neighbors
- Naive Bayes

Among these, the Random Forest Classifier achieved the highest performance. Initially, it had an accuracy of 80.33% and a precision of 80.48%. After fine-tuning the model’s parameters with GridSearchCV, we improved its performance to an accuracy of 81.77% and a precision of 82.16%.

**Benefits of Using This Model**  
- **Accuracy**: The Random Forest Classifier provides reliable predictions, crucial for making informed health decisions.
- **Reliability**: Its ensemble nature ensures stable predictions and minimizes errors.
- **Interpretability**: The model allows us to identify key factors influencing health outcomes despite its complexity.

This enhanced model contributes to better maternity health predictions, aiding healthcare professionals in making more informed decisions.
    """)
