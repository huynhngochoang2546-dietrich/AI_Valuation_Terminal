import pandas as pd
from io import BytesIO



def export_excel(
    ticker,
    price,
    stats,
    forecast,
    simulation,
    risk,
    summary
):


    output = BytesIO()


    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:


        # Summary

        pd.DataFrame(
            summary.items(),
            columns=[
                "Metric",
                "Value"
            ]

        ).to_excel(
            writer,
            sheet_name="Summary",
            index=False
        )



        # Raw price data

        price.to_frame(
            "Close"
        ).to_excel(
            writer,
            sheet_name="Market Data"
        )



        # Statistics

        pd.DataFrame(
            stats.items(),
            columns=[
                "Metric",
                "Value"
            ]

        ).to_excel(
            writer,
            sheet_name="Statistics",
            index=False
        )



        # Forecast

        forecast.to_frame(
            "Forecast Price"
        ).to_excel(
            writer,
            sheet_name="Forecast"
        )



        # Monte Carlo

        pd.DataFrame(
            simulation
        ).to_excel(
            writer,
            sheet_name="Monte Carlo",
            index=False
        )



        # Risk

        pd.DataFrame(
            risk.items(),
            columns=[
                "Risk",
                "Value"
            ]

        ).to_excel(
            writer,
            sheet_name="Risk",
            index=False
        )



    output.seek(0)

    return output