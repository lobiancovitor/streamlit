import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(
    page_title="Screener"
)

if st.button("click me"):
    st.write("Hello")

st.write("""## Market Screener""")

st.sidebar.header("Indicators")


@st.cache_data
def load_data():
    return pd.read_csv("ratings.csv")


@st.cache_data
def load_chart(selected_stock):
    data = yf.download(f"{selected_stock}.SA", start="2022-01-01", end="2024-08-31")
    data["MA(20)"] = data["Close"].rolling(window=20).mean()

    return data


st.subheader("Stocks")

data = load_data()

st.dataframe(data, width=1200, height=600)

stocks = data["Ticker"].tolist()
selected_stock = st.selectbox("Select a stock", stocks)

if stocks:
    st.subheader("Chart")
    data = load_chart(selected_stock)
    chart_data = data[["Close", "MA(20)"]]

    st.line_chart(chart_data)
