def analyst_score(
    stats,
    fundamentals
):

    score=0


    # profitability

    if fundamentals.get(
        "Net Margin",0
    ) > 0.15:

        score+=1



    if fundamentals.get(
        "ROE",0
    ) > 0.15:

        score+=1



    # risk

    if stats["Sharpe Ratio"] > 1:

        score+=1


    if stats["Beta"] < 1.3:

        score+=1



    # valuation

    pe=fundamentals.get(
        "PE Ratio",
        999
    )


    if pe < 25:

        score+=1



    return score