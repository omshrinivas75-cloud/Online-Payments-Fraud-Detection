import pickle
import numpy as np
import pandas as pd
import streamlit as st


with open("encoder.pkl","rb") as file_1:
    encoder = pickle.load(file_1)

with open("model.pkl","rb") as file_2:
    model = pickle.load(file_2)
 

col1, col2 = st.columns([2, 5])
with col1:
        st.image(
            "online-payment-fraud-detection-concept-260nw-2801383859.webp", 
            caption = "Payment", 
            use_container_width = True,
            width = 270
        )

with col2:
    st.title("Online Payments Fraud Detection")


Type = st.selectbox(
    "Payment type",
    ['CASH_IN', 'CASH_OUT',"DEBIT" ,'PAYMENT', 'TRANSFER']
)

amount = st.number_input(
    "Amount",
    min_value=0.0,
    value=0.0,
    step=10000.0
)

col1, col2 = st.columns([3,3])

with col1: 
    oldbalanceOrg = st.number_input(
    "Old Balance",
    min_value=0.0,
    value=0.0,
    step=10000.0
)
    
with col2:
    newbalanceOrig = st.number_input(
    "New Balance",
    min_value=0.0,
    value=0.0,
    step=10000.0
)

button = st.button("Find !")

if button is True:

    encoded_type = encoder.transform([Type])[0]
    prediction = model.predict([[encoded_type,amount,oldbalanceOrg,newbalanceOrig]])

    if prediction == 1:
        st.error("🚨 Fraud Transaction Detected!")
    else:
        st.info("ℹ️ Legitimate Transaction")

    