# analytics/analyst.py


def generate_comment(
    ticker,
    current_price,
    expected_price,
    probability,
    volatility,
    beta,
    sharpe
):

    comment=[]


    upside = (
        expected_price-current_price
    ) / current_price



    # Valuation view

    if upside > 0.15:

        comment.append(
            f"{ticker} appears undervalued. "
            f"Monte Carlo expected value suggests "
            f"potential upside of {upside*100:.2f}%."
        )


    elif upside < -0.15:

        comment.append(
            f"{ticker} appears relatively expensive "
            f"based on simulated valuation."
        )


    else:

        comment.append(
            f"{ticker} is trading close to its estimated value."
        )



    # Risk

    if volatility > 0.35:

        comment.append(
            "Risk level is high because annualized volatility "
            "is above 35%."
        )

    elif volatility > 0.2:

        comment.append(
            "Risk level is moderate."
        )

    else:

        comment.append(
            "Price volatility is relatively stable."
        )



    # Beta

    if beta > 1.2:

        comment.append(
            "The stock is more sensitive than the market "
            "(high beta)."
        )

    elif beta < 0.8:

        comment.append(
            "The stock behaves defensively compared with the market."
        )



    # Probability

    if probability > 0.6:

        comment.append(
            "Monte Carlo distribution shows a positive expected bias."
        )

    else:

        comment.append(
            "Future price uncertainty remains significant."
        )



    # Sharpe

    if sharpe > 1:

        comment.append(
            "Risk-adjusted return looks attractive."
        )

    else:

        comment.append(
            "Risk-adjusted return should be monitored."
        )


    return "\n\n".join(comment)