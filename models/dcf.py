def get_fcf(cashflow):


    operating=cashflow.loc[
    "Operating Cash Flow"
    ]


    capex=cashflow.loc[
    "Capital Expenditure"
    ]


    return (
    operating+capex
    ).dropna()



def terminal_growth(
    revenue_growth,
    roic
):


    reinvestment=(
        revenue_growth/roic
    )


    return (
        roic*
        reinvestment
    )



def dcf(
    fcf,
    wacc,
    g,
    cash,
    debt,
    shares
):


    pv=0


    for i,x in enumerate(fcf):

        pv+=(
        x/
        (1+wacc)**(i+1)
        )


    terminal=(
    fcf.iloc[-1]
    *
    (1+g)
    /
    (wacc-g)
    )


    enterprise=(
    pv+
    terminal/(1+wacc)**len(fcf)
    )


    equity=(
    enterprise+
    cash-
    debt
    )


    return (
    equity/shares
    )