import streamlit as st
import plotly.graph_objects as go

from analytics.export_excel import export_excel

from analytics.charts import (
    price_chart,
    moving_average_chart,
    forecast_chart,
    monte_carlo_chart
)

from analytics.fundamentals import get_fundamentals

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

fundamental = get_fundamentals(
    ticker
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

st.subheader(
    "Monte Carlo Simulation"
)


st.plotly_chart(
    monte_carlo_chart(
        paths
    ),
    use_container_width=True
)

# ==================
# FORECAST
# ==================

forecast=price_forecast(
    price,
    252
)

st.subheader(
    "Forecast"
)


st.plotly_chart(
    forecast_chart(
        price,
        forecast
    ),
    use_container_width=True
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

st.subheader(
    "Export Report"
)



excel_file = export_excel(

    ticker,

    price,

    stats,

    forecast,

    paths,

    {
        "VaR": VaR(paths),
        "Probability Up": probability
    },

    {
        "Current Price": current,
        "Expected Price": final_prices.mean(),
        "Upside":
        (final_prices.mean()-current)/current
    }

)


st.download_button(

    label="Download Excel Report",

    data=excel_file,

    file_name=
    f"{ticker}_Valuation_Report.xlsx",

    mime=
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

)
st.subheader(
    "Fundamental Analysis"
)


st.dataframe(

    pd.DataFrame(
        fundamental.items(),
        columns=[
            "Metric",
            "Value"
        ]

    )

)

import streamlit as st


st.subheader(
    "Price Analysis"
)


st.plotly_chart(
    price_chart(price),
    use_container_width=True
)



st.plotly_chart(
    moving_average_chart(price),
    use_container_width=True
)
