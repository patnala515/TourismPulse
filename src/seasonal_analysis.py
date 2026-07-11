import pandas as pd


class SeasonalAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            print("Tourism data loaded successfully.")
        except Exception as e:
            print("Error loading tourism data:", e)

    def analyze_seasonal_visitors(self):
        seasonal_data = (
            self.df.groupby("season")[
                [
                    "domestic_tourists",
                    "foreign_tourists",
                    "total_tourists"
                ]
            ]
            .sum()
            .sort_values("total_tourists", ascending=False)
        )

        print("\nVisitor Patterns Across Seasons:")
        print(seasonal_data)

        return seasonal_data

    def identify_popular_season(self, seasonal_data):
        peak_season = seasonal_data["total_tourists"].idxmax()
        low_season = seasonal_data["total_tourists"].idxmin()

        print("\nSeason with Highest Visitors:")
        print(peak_season)

        print("\nSeason with Lowest Visitors:")
        print(low_season)

    def analyze_seasonal_preferences(self):
        preference_data = self.df.pivot_table(
            index="season",
            columns="purpose_of_visit",
            values="total_tourists",
            aggfunc="sum"
        )

        print("\nVisitor Preferences Across Seasons:")
        print(preference_data)

        return preference_data


if __name__ == "__main__":

    file_path = "data/processed/cleaned_tourism_data.csv"

    analyzer = SeasonalAnalyzer(file_path)

    analyzer.load_data()

    seasonal_data = analyzer.analyze_seasonal_visitors()

    analyzer.identify_popular_season(seasonal_data)

    analyzer.analyze_seasonal_preferences()