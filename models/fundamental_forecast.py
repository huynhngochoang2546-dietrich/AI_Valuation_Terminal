import numpy as np



def revenue_forecast(
    revenue,
    years=5
):


    growth=[]


    for i in range(
        len(revenue)-1
    ):

        g=(
        revenue.iloc[i]
        /
        revenue.iloc[i+1]
        )-1


        growth.append(g)



    avg_growth=np.mean(
        growth
    )



    future=[]


    current=float(
        revenue.iloc[0]
    )


    for i in range(years):

        current *= (
        1+avg_growth
        )

        future.append(
            current
        )


    return future