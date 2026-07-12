import pandas as pd
import matplotlib.pyplot as plt
import os


class TourismDashboard:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.output_folder = "reports/charts"

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            os.makedirs(self.output_folder, exist_ok=True)

            print("Tourism data loaded successfully.")
            return True

        except Exception as e:
            print("Error loading tourism data:", e)
            return False

    def seasonal_chart(self):
        seasonal_data = (
            self.df.groupby("season")["total_tourists"]
            .sum()
            .sort_values(ascending=False)
        )

        plt.figure(figsize=(8, 5))
        seasonal_data.plot(kind="bar")

        plt.title("Tourist Visitors Across Seasons")
        plt.xlabel("Season")
        plt.ylabel("Total Tourists")
        plt.xticks(rotation=0)
        plt.tight_layout()

        plt.savefig(
            f"{self.output_folder}/seasonal_visitors.png"
        )

        plt.show()
        plt.close()

    def monthly_trend_chart(self):
        month_order = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]

        monthly_data = (
            self.df.groupby("month")["total_tourists"]
            .sum()
            .reindex(month_order)
        )

        plt.figure(figsize=(10, 5))
        monthly_data.plot(kind="line", marker="o")

        plt.title("Monthly Tourism Trend")
        plt.xlabel("Month")
        plt.ylabel("Total Tourists")
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.savefig(
            f"{self.output_folder}/monthly_tourism_trend.png"
        )

        plt.show()
        plt.close()

    def top_destination_chart(self):
        state_data = (
            self.df.groupby("state")["total_tourists"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        plt.figure(figsize=(10, 6))
        state_data.plot(kind="bar")

        plt.title("Top 10 Tourist Destinations")
        plt.xlabel("State")
        plt.ylabel("Total Tourists")
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.savefig(
            f"{self.output_folder}/top_destinations.png"
        )

        plt.show()
        plt.close()

    def purpose_chart(self):
        purpose_data = (
            self.df.groupby("purpose_of_visit")["total_tourists"]
            .sum()
        )

        plt.figure(figsize=(7, 7))

        purpose_data.plot(
            kind="pie",
            autopct="%1.1f%%"
        )

        plt.title("Tourist Preferences by Purpose")
        plt.ylabel("")
        plt.tight_layout()

        plt.savefig(
            f"{self.output_folder}/visitor_preferences.png"
        )

        plt.show()
        plt.close()

    def generate_dashboard(self):
        print("\nGenerating Tourism Analytics Dashboard...")

        self.seasonal_chart()
        self.monthly_trend_chart()
        self.top_destination_chart()
        self.purpose_chart()

        print("\nDashboard charts generated successfully.")
        print(f"Charts saved in: {self.output_folder}")


if __name__ == "__main__":

    file_path = "data/processed/cleaned_tourism_data.csv"

    dashboard = TourismDashboard(file_path)

    if dashboard.load_data():
        dashboard.generate_dashboard()