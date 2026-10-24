# Streamlit Work
import streamlit as st
import pandas as pd
import joblib 

# Load Model 
model = joblib.load('fraud_detection_pipeline.pkl')

st.title("Fraud Detection App")

st.markdown("Please enter the transactions details and use the predict button")

st.divider() 

transaction_type = st.selectbox("Transaction Type" ,["PAYMENT", "TRANSFER", "CASH_OUT", "CASH_IN"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)

oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

# Create Button 
if st.button("Predict"):
    input_data = pd.DataFrame([{
        'type': transaction_type, 
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest, 
        'newbalanceDest': newbalanceDest 
    }])

    prediction = model.predict(input_data)[0] 
    
    st.subheader(f"Prediction: '{int(prediction)}'", divider="gray")
    
    if prediction == 1: 
        st.error("This Transaction can be Fraud!")
    else: 
        st.success("This Transaction look kike it is not a Fraud")
