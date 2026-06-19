import numpy as np
import pandas as pd


def price_forecast(
    price,
    days=252
):

    """
    Forecast future price
    based on historical return
    """


    returns = (
        price
        .pct_change()
        .dropna()
    )


    mu = returns.mean()

    sigma = returns.std()


    current = float(
        price.iloc[-1]
    )


    future_prices=[]


    for i in range(days):

        shock=np.random.normal(
            mu,
            sigma
        )


        current *= (
            1+shock
        )


        future_prices.append(
            current
        )


    future_dates=pd.date_range(
        start=price.index[-1],
        periods=days+1,
        freq="D"
    )[1:]


    forecast=pd.Series(
        future_prices,
        index=future_dates
    )


    return forecast