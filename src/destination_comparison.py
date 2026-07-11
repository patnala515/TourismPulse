import pandas as pd


class DestinationComparator:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            print("Tourism data loaded successfully.")
        except Exception as e:
            print("Error loading tourism data:", e)

    def prepare_destination_data(self):
        destination_data = (
            self.df.groupby("state")
            .agg(
                domestic_tourists=("domestic_tourists", "sum"),
                foreign_tourists=("foreign_tourists", "sum"),
                total_tourists=("total_tourists", "sum"),
                tourism_revenue=("tourism_revenue_inr_crore", "sum"),
                average_growth=("growth_%_approx.", "mean")
            )
            .reset_index()
        )

        return destination_data

    def compare_destinations(self, destination_data):
        print("\nDestination Comparison:")
        print(
            destination_data.sort_values(
                "total_tourists",
                ascending=False
            ).to_string(index=False)
        )

    def top_destinations_by_parameter(self, destination_data):
        parameters = [
            "total_tourists",
            "foreign_tourists",
            "tourism_revenue",
            "average_growth"
        ]

        for parameter in parameters:
            top_destination = destination_data.loc[
                destination_data[parameter].idxmax()
            ]

            print(f"\nTop Destination by {parameter}:")
            print(
                f"{top_destination['state']} - "
                f"{top_destination[parameter]:.2f}"
            )


if __name__ == "__main__":

    file_path = "data/processed/cleaned_tourism_data.csv"

    comparator = DestinationComparator(file_path)

    comparator.load_data()

    destination_data = comparator.prepare_destination_data()

    comparator.compare_destinations(destination_data)

    comparator.top_destinations_by_parameter(destination_data)