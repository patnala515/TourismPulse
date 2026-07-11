import pandas as pd
import os


class TourismDataCleaner:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_excel(self.file_path)
            print("Dataset loaded successfully.")
        except Exception as e:
            print("Error loading dataset:", e)

    def remove_duplicates(self):
        duplicate_count = self.df.duplicated().sum()

        print("Duplicate rows:", duplicate_count)

        self.df.drop_duplicates(inplace=True)

    def clean_column_names(self):
        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace("(", "", regex=False)
            .str.replace(")", "", regex=False)
        )

        print("Column names cleaned successfully.")

    def add_season(self):
        season_map = {
    "December": "Winter",
    "January": "Winter",
    "February": "Winter",
    "March": "Summer",
    "April": "Summer",
    "May": "Summer",
    "June": "Monsoon",
    "July": "Monsoon",
    "August": "Monsoon",
    "September": "Monsoon",
    "October": "Post-Monsoon",
    "November": "Post-Monsoon"
}

        self.df["season"] = self.df["month"].map(season_map)

        print("Season column added successfully.")

    def save_cleaned_data(self, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        self.df.to_csv(output_path, index=False)

        print("Cleaned dataset saved successfully.")


if __name__ == "__main__":

    input_file = "data/raw/India_Tourism_2025.xlsx"

    output_file = "data/processed/cleaned_tourism_data.csv"

    cleaner = TourismDataCleaner(input_file)

    cleaner.load_data()
    cleaner.remove_duplicates()
    cleaner.clean_column_names()
    cleaner.add_season()
    cleaner.save_cleaned_data(output_file)

    print("\nCleaned Dataset Preview:")
    print(cleaner.df.head())

    print("\nCleaned Columns:")
    print(cleaner.df.columns.tolist())