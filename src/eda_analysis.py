import pandas as pd


class TourismEDA:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            print("Cleaned dataset loaded successfully.")
        except Exception as e:
            print("Error loading dataset:", e)

    def dataset_summary(self):
        print("\nDataset Shape:")
        print(self.df.shape)

        print("\nDataset Information:")
        self.df.info()

        print("\nStatistical Summary:")
        print(self.df.describe())

    def tourist_summary(self):
        print("\nTotal Domestic Tourists:")
        print(self.df["domestic_tourists"].sum())

        print("\nTotal Foreign Tourists:")
        print(self.df["foreign_tourists"].sum())

        print("\nTotal Tourists:")
        print(self.df["total_tourists"].sum())

        print("\nTotal Tourism Revenue (INR Crore):")
        print(self.df["tourism_revenue_inr_crore"].sum())

    def top_states(self):
        state_data = (
            self.df.groupby("state")["total_tourists"]
            .sum()
            .sort_values(ascending=False)
        )

        print("\nTop 10 States by Total Tourists:")
        print(state_data.head(10))

    def purpose_analysis(self):
        print("\nPurpose of Visit:")
        print(self.df["purpose_of_visit"].value_counts())


if __name__ == "__main__":

    file_path = "data/processed/cleaned_tourism_data.csv"

    eda = TourismEDA(file_path)

    eda.load_data()
    eda.dataset_summary()
    eda.tourist_summary()
    eda.top_states()
    eda.purpose_analysis()