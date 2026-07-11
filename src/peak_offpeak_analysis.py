import pandas as pd


class PeakOffPeakAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            print("Tourism data loaded successfully.")
        except Exception as e:
            print("Error loading tourism data:", e)

    def analyze_monthly_visitors(self):
        monthly_data = (
            self.df.groupby("month")["total_tourists"]
            .sum()
            .sort_values(ascending=False)
        )

        print("\nMonthly Tourist Analysis:")
        print(monthly_data)

        return monthly_data

    def identify_peak_offpeak(self, monthly_data):
        peak_month = monthly_data.idxmax()
        peak_visitors = monthly_data.max()

        offpeak_month = monthly_data.idxmin()
        offpeak_visitors = monthly_data.min()

        print("\nPeak Travel Period:")
        print(f"{peak_month} - {peak_visitors} tourists")

        print("\nOff-Peak Travel Period:")
        print(f"{offpeak_month} - {offpeak_visitors} tourists")

    def top_peak_months(self, monthly_data):
        print("\nTop 3 Peak Travel Months:")
        print(monthly_data.head(3))

        print("\nTop 3 Off-Peak Travel Months:")
        print(monthly_data.tail(3).sort_values())


if __name__ == "__main__":

    file_path = "data/processed/cleaned_tourism_data.csv"

    analyzer = PeakOffPeakAnalyzer(file_path)

    analyzer.load_data()

    monthly_data = analyzer.analyze_monthly_visitors()

    analyzer.identify_peak_offpeak(monthly_data)

    analyzer.top_peak_months(monthly_data)