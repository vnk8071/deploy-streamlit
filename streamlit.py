import streamlit as st
import numpy as np
import pandas as pd
from src.dataset import label_encoder
from src.StrokeDetector  import StrokeDectector
import warnings
warnings.filterwarnings("ignore")

# Page settings
st.set_page_config(page_title="Stroke Prediction", layout="wide")

st.title("Stroke Prediction")
st.write("""
## The project to predict the risk of stroke \n
The data was collected from Kaggle Community. \n
Link: https://www.kaggle.com/fedesoriano/stroke-prediction-dataset
""")
st.markdown('**_For information_**: https://github.com/vnk8071')
st.write("------------------------------------------------------------------------------------")
st.write("Please set your profile to predict")


def input_user():
    '''
    Input: The status of patient like gender, age, etc.

    Return: Type ndarray of patient healthcare status [0, 1, etc]
    '''
    col1, col2 = st.beta_columns(2)
    with col1:
    # Input parameter
        gender = st.selectbox("Select gender", ("Male", "Female"))
        age = float(st.slider("Select age",1,100))
        avg_glucose = float(st.slider("The glucose level",50,250))
        bmi_value = float(st.slider("The BMI value", 10, 50))

    with col2:
        residence = st.selectbox("Type of residence", ("Rural", "Urban"))
        hypertension = st.selectbox("Hypertension", ("Yes", "No"))
        heart_disease = st.selectbox("Heart Disease",("Yes", "No"))
        smoking = st.selectbox("The smoking status", ("formerly smoked", "never smoked",\
                                                      "smokes", "Unknown"))

    # Change into array
    patient_infor = {"gender": [gender],"age": [age], "hypertension": [hypertension],\
                "heart_disease": [heart_disease], "Residence_type": [residence],\
                "avg_glucose_level": [avg_glucose], "bmi": [bmi_value],\
                "smoking_status": [smoking]}
    patient_infor = pd.DataFrame(patient_infor)
    return patient_infor

def preprocess(patient_infor):
    patient = label_encoder(patient_infor)
    patient = np.array(patient)
    return patient


if __name__ == '__main__':
    
    # Input of patient
    patient_infor = input_user()
    patient = preprocess(patient_infor)
    st.write("------------------------------------------------------------------------------------")
    footer_col1, footer_col2 = st.beta_columns([1,3]) 
    with footer_col1:
        classifier_model = st.selectbox("Select model predict",("Logistic Regression",\
                            "LightGBM Classifier", "Random Forest", "XGB Classifier",\
                            "Adaboosting Classifier", "Decision Tree"))
        st.write("The model prediction:")
        st.write(classifier_model)
        
    with footer_col2:
        st.write("The input of patient")
        st.write(patient_infor)

    # Start to predict
    start = st.button("Start predict")
    if start == True:
        output = StrokeDectector(classifier_model)
        output = output.predict(patient)
        st.write("The result of predict: ", output)
        st.success("Done :sunglasses:")
    else:
        st.write("Set patient profile again")

