import yfinance as yf
import pandas as pd
import streamlit as st



@st.cache_data(ttl=3600)
def get_price(ticker):


    data=yf.download(
        ticker,
        period="10y",
        auto_adjust=True,
        progress=False
    )


    price=data["Close"]


    if isinstance(price,pd.DataFrame):
        price=price.iloc[:,0]


    return price



@st.cache_data(ttl=3600)
def get_market():

    return get_price("^GSPC")



@st.cache_data(ttl=3600)
def get_risk_free():

    data=yf.download(
        "^TNX",
        period="5d",
        progress=False
    )


    rate=data["Close"]


    if isinstance(rate,pd.DataFrame):
        rate=rate.iloc[:,0]


    return float(
        rate.iloc[-1]
    )/100
