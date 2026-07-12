import pandas as pd


class DemographicAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            print("Demographic data loaded successfully.")
            return True

        except Exception as e:
            print("Error loading demographic data:", e)
            return False

    def analyze_gender(self):
        gender_data = self.df[
            self.df["demographic_type"] == "Gender"
        ]

        print("\nGender-Wise Tourist Demographics:")
        print(
            gender_data[
                ["category", "percentage"]
            ].to_string(index=False)
        )

        top_gender = gender_data.loc[
            gender_data["percentage"].idxmax()
        ]

        print(
            f"\nHighest Gender Category: "
            f"{top_gender['category']} - "
            f"{top_gender['percentage']:.2f}%"
        )

    def analyze_age_groups(self):
        age_data = self.df[
            self.df["demographic_type"] == "Age"
        ]

        print("\nAge-Wise Tourist Demographics:")
        print(
            age_data[
                ["category", "percentage"]
            ].to_string(index=False)
        )

        top_age_group = age_data.loc[
            age_data["percentage"].idxmax()
        ]

        print(
            f"\nMost Common Age Group: "
            f"{top_age_group['category']} - "
            f"{top_age_group['percentage']:.2f}%"
        )


if __name__ == "__main__":

    file_path = "data/raw/tourist_demographics.csv"

    analyzer = DemographicAnalyzer(file_path)

    if analyzer.load_data():
        analyzer.analyze_gender()
        analyzer.analyze_age_groups()