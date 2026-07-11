import pandas as pd


class VisitorAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            print("Tourism data loaded successfully.")
        except Exception as e:
            print("Error loading tourism data:", e)

    def analyze_visit_preferences(self):
        preference_data = (
            self.df.groupby("purpose_of_visit")["total_tourists"]
            .sum()
            .sort_values(ascending=False)
        )

        print("\nVisitor Preferences by Purpose of Visit:")
        print(preference_data)

        most_preferred = preference_data.idxmax()

        print("\nMost Preferred Purpose of Visit:")
        print(most_preferred)

        return preference_data

    def analyze_domestic_foreign_visitors(self):
        domestic = self.df["domestic_tourists"].sum()
        foreign = self.df["foreign_tourists"].sum()

        print("\nVisitor Category Analysis:")
        print(f"Domestic Tourists: {domestic}")
        print(f"Foreign Tourists: {foreign}")

        if domestic > foreign:
            print("Domestic tourists are the dominant visitor category.")
        else:
            print("Foreign tourists are the dominant visitor category.")

    def analyze_state_preferences(self):
        state_preferences = (
            self.df.groupby(["state", "purpose_of_visit"])["total_tourists"]
            .sum()
            .reset_index()
        )

        top_preferences = state_preferences.loc[
            state_preferences.groupby("state")["total_tourists"].idxmax()
        ]

        print("\nMost Popular Visit Purpose by State:")
        print(
            top_preferences[
                ["state", "purpose_of_visit", "total_tourists"]
            ].to_string(index=False)
        )

        return top_preferences


if __name__ == "__main__":

    file_path = "data/processed/cleaned_tourism_data.csv"

    analyzer = VisitorAnalyzer(file_path)

    analyzer.load_data()

    analyzer.analyze_visit_preferences()

    analyzer.analyze_domestic_foreign_visitors()

    analyzer.analyze_state_preferences()