import numpy as np



def simulate(
    price,
    days=252,
    runs=10000
):


    returns = (
        price
        .pct_change()
        .dropna()
    )


    mu = returns.mean()*252

    sigma = returns.std()*np.sqrt(252)


    S0=float(
        price.iloc[-1]
    )


    paths=np.zeros(
        (days+1,runs)
    )


    paths[0]=S0



    dt=1/252


    for t in range(1,days+1):


        Z=np.random.normal(
            0,
            1,
            runs
        )


        paths[t]=(
            paths[t-1]
            *
            np.exp(
                (
                    mu-
                    0.5*sigma**2
                )
                *
                dt
                +
                sigma*np.sqrt(dt)*Z
            )
        )


    return paths