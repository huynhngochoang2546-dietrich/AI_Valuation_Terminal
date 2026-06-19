import numpy as np



def VaR(paths):

    final=paths[-1]

    return np.percentile(
        final,
        5
    )



def probability_up(
    paths,
    current
):

    return (
        paths[-1]
        >
        current
    ).mean()