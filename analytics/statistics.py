import numpy as np



def statistics(
    price,
    market
):


    stock_return = (
        price
        .pct_change()
        .dropna()
    )


    market_return=(
        market
        .pct_change()
        .dropna()
    )



    volatility=(
        stock_return.std()
        *
        np.sqrt(252)
    )



    beta=(
        np.cov(
        stock_return,
        market_return[-len(stock_return):]
        )[0][1]
        /
        np.var(
        market_return[-len(stock_return):]
        )
    )



    sharpe=(
        stock_return.mean()
        *
        252
        /
        volatility
    )


    return {

    "Annual Return":
        stock_return.mean()*252,


    "Volatility":
        volatility,


    "Beta":
        beta,


    "Sharpe Ratio":
        sharpe,


    "Max Daily Loss":
        stock_return.min()

    }