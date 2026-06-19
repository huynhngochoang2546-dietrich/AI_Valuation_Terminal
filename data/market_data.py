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


# SỬA ĐOẠN NÀY TRONG FILE data/market_data.py (Dòng 19 - 26)
    
    # 1. Đảm bảo loại bỏ hoàn toàn cấu trúc MultiIndex nếu yfinance tự sinh ra
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1) # Bỏ tầng dưới (tầng chứa tên Ticker)

    # 2. Lấy cột Close an toàn và loại bỏ các dòng trống ở cuối (nếu có)
    price = data["Close"].dropna()

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
