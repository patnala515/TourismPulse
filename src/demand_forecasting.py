import pandas as pd
import numpy as np
from datetime import datetime


class TourismDemandForecaster:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            print("Tourism data loaded successfully.")
        except Exception as e:
            print("Error loading tourism data:", e)

    def prepare_monthly_data(self):
        month_order = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]

        monthly_data = (
            self.df.groupby("month")["total_tourists"]
            .sum()
            .reindex(month_order)
            .reset_index()
        )

        monthly_data["month_number"] = np.arange(
            1, len(monthly_data) + 1
        )

        print("\nHistorical Monthly Tourist Demand:")
        print(monthly_data[["month", "total_tourists"]].to_string(index=False))

        return monthly_data

    def calculate_trend(self, monthly_data):
        x = monthly_data["month_number"]
        y = monthly_data["total_tourists"]

        slope, intercept = np.polyfit(x, y, 1)

        print("\nTourism Demand Trend:")
        print(f"Monthly Trend Growth: {slope:.2f}")

        if slope > 0:
            print("Tourist demand shows an increasing trend.")
        elif slope < 0:
            print("Tourist demand shows a decreasing trend.")
        else:
            print("Tourist demand shows a stable trend.")

        return slope, intercept

    def forecast_future_demand(
        self,
        monthly_data,
        slope,
        intercept,
        forecast_months=3
    ):
        future_month_numbers = np.arange(
            len(monthly_data) + 1,
            len(monthly_data) + forecast_months + 1
        )

        forecast_values = (
            slope * future_month_numbers + intercept
        )

        forecast_values = np.maximum(
            forecast_values,
            0
        ).astype(int)

        last_date = datetime(2025, 12, 1)

        future_months = []

        for i in range(1, forecast_months + 1):
            month_number = ((last_date.month - 1 + i) % 12) + 1
            year = last_date.year + ((last_date.month - 1 + i) // 12)

            future_date = datetime(year, month_number, 1)

            future_months.append(
                future_date.strftime("%B %Y")
            )

        forecast_data = pd.DataFrame({
            "future_month": future_months,
            "predicted_tourists": forecast_values
        })

        print("\nFuture Tourist Demand Forecast:")
        print(forecast_data.to_string(index=False))

        return forecast_data


if __name__ == "__main__":

    file_path = "data/processed/cleaned_tourism_data.csv"

    forecaster = TourismDemandForecaster(file_path)

    forecaster.load_data()

    monthly_data = forecaster.prepare_monthly_data()

    slope, intercept = forecaster.calculate_trend(
        monthly_data
    )

    forecast_data = forecaster.forecast_future_demand(
        monthly_data,
        slope,
        intercept
    )