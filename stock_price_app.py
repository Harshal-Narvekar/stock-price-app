import streamlit as st
import pandas as pd
import quandl

# Quandl API Key
quandl_api_key = 'y56MqrbLxPrge17vrjx4'  # Replace with your actual Quandl API key

# Title
st.title("Indian Stock Price Web App")

# Sidebar
stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., BSE/BOM500325 for TCS)", "BSE/BOM500325")
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

# Set target price
target_price = st.sidebar.number_input("Enter Target Price", value=0.0, step=1.0)

# Function to fetch stock data from Quandl
def fetch_stock_data(symbol, start, end):
    try:
        quandl.ApiConfig.api_key = quandl_api_key
        data = quandl.get(symbol, start_date=start, end_date=end)
        return data
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

# Function to trigger alert when stock reaches target price
def alert_on_target_price(data, target):
    try:
        latest_price = data['Close'].iloc[-1]
        if latest_price >= target:
            st.sidebar.text(f"🚨 Alert: {stock_symbol} reached or exceeded the target price of {latest_price}")
    except Exception as e:
        st.error(f"An error occurred while checking the target price: {str(e)}")

# Fetch stock data
data = fetch_stock_data(stock_symbol, start_date, end_date)

# Display stock data if available
if data is not None:
    st.write("### Stock Data")
    st.write(data)

    # Display stock chart
    st.write(f"### {stock_symbol} Stock Price")
    st.line_chart(data['Close'])

    # Check and trigger alert if stock reaches target price
    alert_on_target_price(data, target_price)

# Footer
st.text("Developed By Harshal Narvekar & Built with Streamlit")


