def generate_comment(
    ticker,
    current,
    expected,
    probability,
    volatility,
    beta,
    sharpe
):


    upside = (
        expected-current
    )/current



    comments=[]



    # Valuation

    if upside > 0.15:

        comments.append(
        f"{ticker} appears undervalued "
        f"with estimated upside of {upside*100:.1f}%."
        )

    elif upside < -0.15:

        comments.append(
        f"{ticker} appears overvalued "
        f"based on current projection."
        )

    else:

        comments.append(
        f"{ticker} is trading close to estimated value."
        )



    # Risk

    if volatility > 0.35:

        comments.append(
        "Risk is high due to elevated volatility."
        )

    else:

        comments.append(
        "Volatility remains within a moderate range."
        )



    # Beta

    if beta > 1.3:

        comments.append(
        "Stock is more sensitive to market movements."
        )


    elif beta < 0.8:

        comments.append(
        "Stock has defensive characteristics."
        )


    # Probability

    if probability > 0.6:

        comments.append(
        "Monte Carlo simulation shows positive probability bias."
        )

    else:

        comments.append(
        "Future price distribution remains uncertain."
        )



    # Sharpe

    if sharpe > 1:

        comments.append(
        "Risk-adjusted return is attractive."
        )


    return "\n\n".join(comments)