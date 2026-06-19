import yfinance as yf



def get_statement(ticker):

    stock=yf.Ticker(ticker)


    return {

    "income":
        stock.financials,


    "balance":
        stock.balance_sheet,


    "cashflow":
        stock.cashflow,


    "info":
        stock.info

    }