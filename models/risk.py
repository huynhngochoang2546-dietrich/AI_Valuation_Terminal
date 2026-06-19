import numpy as np


def beta(stock,market):

    return (
        np.cov(
        stock,
        market
        )[0][1]
        /
        np.var(market)
    )



def cost_equity(
    rf,
    beta,
    market_return
):

    return (
    rf+
    beta*
    (market_return-rf)
    )