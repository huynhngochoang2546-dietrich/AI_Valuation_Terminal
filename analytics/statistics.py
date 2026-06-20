import numpy as np
import pandas as pd



def statistics(price, market):


    # convert dataframe -> series
    if isinstance(price, pd.DataFrame):

        price = price.iloc[:,0]


    if isinstance(market, pd.DataFrame):

        market = market.iloc[:,0]



    # returns

    stock_return = (
        price
        .pct_change()
        .dropna()
    )


    market_return = (
        market
        .pct_change()
        .dropna()
    )



    # align dates

    df = pd.concat(
        [
            stock_return,
            market_return
        ],
        axis=1
    ).dropna()



    stock_return = df.iloc[:,0]
    market_return = df.iloc[:,1]



    # ==================
    # Beta
    # ==================

    covariance = np.cov(
        stock_return.values,
        market_return.values
    )[0,1]


    variance = np.var(
        market_return.values
    )


    beta = covariance / variance



    # ==================
    # metrics
    # ==================


    annual_return = (
        stock_return.mean()
        *252
    )


    volatility = (
        stock_return.std()
        *
        np.sqrt(252)
    )


    sharpe = (
        annual_return /
        volatility
    )



    # drawdown

    cumulative = (
        1+stock_return
    ).cumprod()


    peak = cumulative.cummax()


    drawdown = (
        cumulative-peak
    )/peak



    max_drawdown = drawdown.min()



    return {

        "Annual Return":
        float(annual_return),


        "Volatility":
        float(volatility),


        "Beta":
        float(beta),


        "Sharpe Ratio":
        float(sharpe),


        "Max Daily Loss":
        float(max_drawdown)

    }
