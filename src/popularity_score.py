import pandas as pd
import numpy as np


class PopularityScoreAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            print("Tourism data loaded successfully.")
        except Exception as e:
            print("Error loading tourism data:", e)

    def calculate_popularity_score(self):
        destination_data = (
            self.df.groupby("state")
            .agg(
                total_tourists=("total_tourists", "sum"),
                tourism_revenue=("tourism_revenue_inr_crore", "sum"),
                average_growth=("growth_%_approx.", "mean")
            )
            .reset_index()
        )

        destination_data["tourist_score"] = (
            destination_data["total_tourists"]
            / destination_data["total_tourists"].max()
        ) * 100

        destination_data["revenue_score"] = (
            destination_data["tourism_revenue"]
            / destination_data["tourism_revenue"].max()
        ) * 100

        min_growth = destination_data["average_growth"].min()
        max_growth = destination_data["average_growth"].max()

        destination_data["growth_score"] = np.where(
            max_growth == min_growth,
            100,
            (
                (destination_data["average_growth"] - min_growth)
                / (max_growth - min_growth)
            ) * 100
        )

        destination_data["popularity_score"] = (
            destination_data["tourist_score"] * 0.50
            + destination_data["revenue_score"] * 0.30
            + destination_data["growth_score"] * 0.20
        )

        destination_data = destination_data.sort_values(
            "popularity_score",
            ascending=False
        )

        print("\nDestination Popularity Scores:")
        print(
            destination_data[
                [
                    "state",
                    "total_tourists",
                    "tourism_revenue",
                    "average_growth",
                    "popularity_score"
                ]
            ].to_string(index=False)
        )

        return destination_data

    def display_top_destinations(self, destination_data):
        print("\nTop 10 Popular Tourist Destinations:")

        print(
            destination_data[
                ["state", "popularity_score"]
            ].head(10).to_string(index=False)
        )


if __name__ == "__main__":

    file_path = "data/processed/cleaned_tourism_data.csv"

    analyzer = PopularityScoreAnalyzer(file_path)

    analyzer.load_data()

    popularity_data = analyzer.calculate_popularity_score()

    analyzer.display_top_destinations(popularity_data)