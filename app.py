import streamlit as st
import plotly.graph_objects as go

from analytics.export_excel import export_excel

from data.market_data import *

from models.monte_carlo import simulate

from analytics.statistics import statistics

from analytics.forecast import price_forecast

from analytics.metrics import (
    VaR,
    probability_up
)

from analytics.analyst import generate_comment



st.set_page_config(
    page_title="Valuation Terminal",
    layout="wide"
)



st.title(
    "📈 Stock Valuation Terminal"
)



ticker = st.sidebar.text_input(
    "Enter Stock Ticker",
    "AAPL"
)



# ==================
# DATA
# ==================

try:

    price=get_price(ticker)

except:

    st.error(
    "Invalid ticker or no data available"
    )

    st.stop()


market=get_market()


current=float(
    price.iloc[-1]
)



# ==================
# STATISTICS
# ==================

stats=statistics(
    price,
    market
)



# ==================
# MONTE CARLO
# ==================

paths=simulate(
    price,
    days=252,
    runs=5000
)


final_prices=paths[-1]


probability=probability_up(
    paths,
    current
)



# ==================
# FORECAST
# ==================

forecast=price_forecast(
    price,
    252
)



# ==================
# AI COMMENT
# ==================

comment=generate_comment(

    ticker,

    current,

    final_prices.mean(),

    probability,

    stats["Volatility"],

    stats["Beta"],

    stats["Sharpe Ratio"]

)



# ==================
# TOP STAT CARDS
# ==================

st.subheader(
    "Market Statistics"
)


c1,c2,c3,c4,c5=st.columns(5)


c1.metric(
    "Price",
    f"${current:.2f}"
)


c2.metric(
    "Return",
    f"{stats['Annual Return']*100:.2f}%"
)


c3.metric(
    "Volatility",
    f"{stats['Volatility']*100:.2f}%"
)


c4.metric(
    "Beta",
    f"{stats['Beta']:.2f}"
)


c5.metric(
    "Sharpe",
    f"{stats['Sharpe Ratio']:.2f}"
)



# ==================
# HISTORY
# ==================

st.subheader(
    "Historical Price"
)


st.line_chart(
    price
)



# ==================
# FORECAST
# ==================

st.subheader(
    "252 Days Forecast"
)


st.line_chart(
    forecast
)



# ==================
# MONTE CARLO
# ==================

st.subheader(
    "Monte Carlo Simulation"
)



fig=go.Figure()



for i in range(100):

    fig.add_trace(

        go.Scatter(

            x=list(range(253)),

            y=paths[:,i],

            mode="lines",

            showlegend=False

        )

    )


fig.update_layout(

    height=600,

    xaxis_title="Days",

    yaxis_title="Price"

)


st.plotly_chart(
    fig,
    use_container_width=True
)



# ==================
# MC RESULT
# ==================

st.subheader(
"Simulation Result"
)



a,b,c,d=st.columns(4)


a.metric(
"Expected Price",
f"${final_prices.mean():.2f}"
)


b.metric(
"Best Case",
f"${final_prices.max():.2f}"
)


c.metric(
"Worst Case",
f"${final_prices.min():.2f}"
)


d.metric(
"Probability Up",
f"{probability*100:.2f}%"
)



# ==================
# RISK
# ==================

st.subheader(
"Risk Metrics"
)


st.json({

"VaR 95%":
VaR(paths),

"Max Drawdown":
stats["Max Daily Loss"],

"Beta":
stats["Beta"],

"Volatility":
stats["Volatility"],

"Sharpe":
stats["Sharpe Ratio"]

})



# ==================
# AI COMMENT
# ==================

st.subheader(
"AI Financial Analyst"
)


st.write(
comment
)
