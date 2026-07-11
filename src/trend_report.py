import pandas as pd
import os
from datetime import datetime


class TourismTrendReport:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            print("Tourism data loaded successfully.")
            return True
        except Exception as e:
            print("Error loading tourism data:", e)
            return False

    def generate_insights(self):
        monthly_data = (
            self.df.groupby("month")["total_tourists"]
            .sum()
        )

        seasonal_data = (
            self.df.groupby("season")["total_tourists"]
            .sum()
        )

        state_data = (
            self.df.groupby("state")["total_tourists"]
            .sum()
        )

        purpose_data = (
            self.df.groupby("purpose_of_visit")["total_tourists"]
            .sum()
        )

        peak_month = monthly_data.idxmax()
        offpeak_month = monthly_data.idxmin()
        popular_season = seasonal_data.idxmax()
        top_destination = state_data.idxmax()
        top_purpose = purpose_data.idxmax()

        insights = [
            f"Peak travel month: {peak_month}",
            f"Off-peak travel month: {offpeak_month}",
            f"Most popular tourism season: {popular_season}",
            f"Most visited destination: {top_destination}",
            f"Leading purpose of visit: {top_purpose}",
            f"Total tourists analyzed: {self.df['total_tourists'].sum()}",
            (
                "Total tourism revenue: INR "
                f"{self.df['tourism_revenue_inr_crore'].sum():.2f} Crore"
            )
        ]

        return insights

    def generate_report(self, insights):
        os.makedirs("reports", exist_ok=True)

        report_time = datetime.now()

        report_path = "reports/tourism_trend_report.txt"

        with open(report_path, "w", encoding="utf-8") as report:
            report.write("TOURISMPULSE - TRAVEL TREND REPORT\n")
            report.write("=" * 45 + "\n")

            report.write(
                f"Generated On: "
                f"{report_time.strftime('%d-%m-%Y %H:%M:%S')}\n\n"
            )

            report.write("TOURISM INSIGHTS\n")
            report.write("-" * 30 + "\n")

            for insight in insights:
                report.write(f"- {insight}\n")

        print("\nTravel Trend Report Generated Successfully.")
        print(f"Report saved at: {report_path}")

    def display_insights(self, insights):
        print("\nTourism Trend Insights:")

        for insight in insights:
            print(f"- {insight}")


if __name__ == "__main__":

    file_path = "data/processed/cleaned_tourism_data.csv"

    report_generator = TourismTrendReport(file_path)

    if report_generator.load_data():

        insights = report_generator.generate_insights()

        report_generator.display_insights(insights)

        report_generator.generate_report(insights)