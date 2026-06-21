import yfinance as yf



def get_fundamentals(ticker):

    stock = yf.Ticker(ticker)


    income = stock.financials
    balance = stock.balance_sheet



    result = {}



    # ==================
    # Profitability
    # ==================


    try:

        revenue = income.loc[
            "Total Revenue"
        ][0]


        net_income = income.loc[
            "Net Income"
        ][0]


        gross_profit = income.loc[
            "Gross Profit"
        ][0]



        result["Net Margin"] = (
            net_income / revenue
        )


        result["Gross Margin"] = (
            gross_profit / revenue
        )



    except:

        pass



    # ==================
    # Liquidity
    # ==================

    try:

        current_assets = balance.loc[
            "Current Assets"
        ][0]


        current_liabilities = balance.loc[
            "Current Liabilities"
        ][0]



        result["Current Ratio"] = (
            current_assets /
            current_liabilities
        )


    except:

        pass



    # ==================
    # Solvency
    # ==================

    try:

        debt = balance.loc[
            "Total Debt"
        ][0]


        equity = balance.loc[
            "Stockholders Equity"
        ][0]



        result["Debt To Equity"] = (
            debt / equity
        )


    except:

        pass



    # ==================
    # Valuation
    # ==================

    info = stock.info



    result["PE Ratio"] = (
        info.get(
            "trailingPE",
            None
        )
    )


    result["PB Ratio"] = (
        info.get(
            "priceToBook",
            None
        )
    )


    result["Dividend Yield"] = (
        info.get(
            "dividendYield",
            None
        )
    )


    result["ROE"] = (
        info.get(
            "returnOnEquity",
            None
        )
    )


    result["ROA"] = (
        info.get(
            "returnOnAssets",
            None
        )
    )


    return result