import streamlit as st
import pandas as pd
import joblib

# Title
st.title("HDFC Stock Movement Prediction App")

# Description
st.markdown("""
    Welcome to the **HDFC Stock Movement Prediction App**. This tool predicts whether the closing price of HDFC stocks 
    will **increase**, **decrease**, or **remain the same** based on today's stock data.
    
     ### Instructions:
    - Enter **Today's HDFC stock data** as input for prediction.
    - For reference, you can fetch the stock data from reliable sources such as stock market websites or APIs.
    - You can find the stock data for HDFC Bank here: [NSE HDFC Bank Stock Data](https://www.nseindia.com/get-quotes/equity?symbol=HDFCBANK).
    - The model will predict the **Trend for Tomorrow's closing price** based on the given data.
            
    **Disclaimer:**
    - This model is still under development and is created for educational purposes only.
    - It should not be used for actual trading decisions.
    - Please consult professional financial advisors for trading or investment decisions.
""")
# Input Fields
input = {
    'OPEN ': st.number_input("Today's Opening Price (Open)"),
    'HIGH ': st.number_input("Today's High Price (High)"),
    'LOW ': st.number_input("Today's Low Price (Low)"),
    'PREV. CLOSE ': st.number_input("Yesterday's Closing Price (Previous Close)"),
    'ltp ': st.number_input("Today's Last Traded Price (LTP)"),
    'close ': st.number_input("Today's Closing Price (Close)"),
    'vwap ': st.number_input("Today's Volume Weighted Average Price (VWAP)"),
    '52W H ': st.number_input("52-Week High Price"),
    '52W L ': st.number_input("52-Week Low Price"),
    'VOLUME ': int(st.number_input("Today's Volume")),
    'VALUE ': int(st.number_input("Today's Value")),
    'No of trades ': int(st.number_input("Today's Number of Trades"))
}

# Calculated Feature: Price Change
price_change = input['close '] - input['PREV. CLOSE ']
input['price_change'] = price_change

# Load Model
model = joblib.load("stock_market_prediction_HDFC.pkl")

# Predict Button
if st.button("Predict"):
    try:
        # Convert input dictionary to DataFrame
        X_input = pd.DataFrame(input, index=[0])
        prediction = model.predict(X_input)

        # Display Prediction
        if prediction == 1:
            st.markdown(
                "<h3 style='color: green;'>The closing price of HDFC stock is predicted to increase tomorrow.</h3>",
                unsafe_allow_html=True
            )
        elif prediction == -1:
            st.markdown(
                "<h3 style='color: red;'>The closing price of HDFC stock is predicted to decrease tomorrow.</h3>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<h3 style='color: gray;'>The closing price of HDFC stock is predicted to remain unchanged tomorrow.</h3>",
                unsafe_allow_html=True
            )
    except Exception as e:
        st.error(f"Error during prediction: {e}")
