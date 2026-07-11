import pandas as pd


class EmergingHotspotAnalyzer:

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

    def analyze_destination_growth(self):
        hotspot_data = (
            self.df.groupby("state")
            .agg(
                total_tourists=("total_tourists", "sum"),
                average_growth=("growth_%_approx.", "mean")
            )
            .reset_index()
        )

        return hotspot_data

    def identify_emerging_hotspots(self, hotspot_data):
        average_tourists = hotspot_data["total_tourists"].mean()
        average_growth = hotspot_data["average_growth"].mean()

        emerging_hotspots = hotspot_data[
            (hotspot_data["average_growth"] > average_growth)
            & (hotspot_data["total_tourists"] < average_tourists)
        ]

        emerging_hotspots = emerging_hotspots.sort_values(
            "average_growth",
            ascending=False
        )

        print("\nEmerging Tourist Hotspots:")
        print(
            emerging_hotspots[
                [
                    "state",
                    "total_tourists",
                    "average_growth"
                ]
            ].to_string(index=False)
        )

        return emerging_hotspots

    def display_top_hotspots(self, emerging_hotspots):
        print("\nTop 10 Emerging Tourist Hotspots:")

        print(
            emerging_hotspots[
                ["state", "average_growth"]
            ].head(10).to_string(index=False)
        )


if __name__ == "__main__":

    file_path = "data/processed/cleaned_tourism_data.csv"

    analyzer = EmergingHotspotAnalyzer(file_path)

    if analyzer.load_data():

        hotspot_data = analyzer.analyze_destination_growth()

        emerging_hotspots = analyzer.identify_emerging_hotspots(
            hotspot_data
        )

        analyzer.display_top_hotspots(emerging_hotspots)