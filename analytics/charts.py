import plotly.graph_objects as go
import pandas as pd



def price_chart(price):

    fig = go.Figure()


    fig.add_trace(
        go.Scatter(
            x=price.index,
            y=price.values,
            mode="lines",
            name="Close Price"
        )
    )


    fig.update_layout(
        title="Historical Price",
        xaxis_title="Date",
        yaxis_title="Price",
        height=500
    )


    return fig





def moving_average_chart(price):


    df=pd.DataFrame()

    df["Close"]=price

    df["MA20"]=(
        df.Close
        .rolling(20)
        .mean()
    )

    df["MA50"]=(
        df.Close
        .rolling(50)
        .mean()
    )

    df["MA200"]=(
        df.Close
        .rolling(200)
        .mean()
    )



    fig=go.Figure()


    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df.Close,
            name="Price"
        )
    )


    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df.MA20,
            name="MA20"
        )
    )


    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df.MA50,
            name="MA50"
        )
    )


    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df.MA200,
            name="MA200"
        )
    )



    fig.update_layout(
        title="Moving Average Analysis",
        height=500
    )


    return fig




def forecast_chart(
        price,
        forecast
):

    fig=go.Figure()


    fig.add_trace(
        go.Scatter(
            x=price.index,
            y=price,
            name="Historical"
        )
    )


    fig.add_trace(
        go.Scatter(
            x=forecast.index,
            y=forecast,
            name="Forecast"
        )
    )


    fig.update_layout(
        title="Price Forecast",
        height=500
    )


    return fig




def monte_carlo_chart(simulation):


    final_price = simulation[-1,:]


    fig=go.Figure()


    fig.add_trace(
        go.Histogram(
            x=final_price,
            nbinsx=50,
            name="Simulation"
        )
    )


    fig.update_layout(
        title="Monte Carlo Terminal Price Distribution",
        height=500
    )


    return fig