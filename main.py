from src.logger_config import TourismLogger
from src.eda_analysis import TourismEDA
from src.seasonal_analysis import SeasonalAnalyzer
from src.peak_offpeak_analysis import PeakOffPeakAnalyzer
from src.visitor_analysis import VisitorAnalyzer
from src.demographic_analysis import DemographicAnalyzer
from src.popularity_score import PopularityScoreAnalyzer
from src.demand_forecasting import TourismDemandForecaster
from src.destination_comparison import DestinationComparator
from src.emerging_hotspots import EmergingHotspotAnalyzer
from src.trend_report import TourismTrendReport
from src.visual_dashboard import TourismDashboard


class TourismPulse:

    def __init__(self):
        self.tourism_file = (
            "data/processed/cleaned_tourism_data.csv"
        )

        self.demographic_file = (
            "data/raw/tourist_demographics.csv"
        )

        logger_config = TourismLogger()
        self.logger = logger_config.setup_logger()

    def display_menu(self):
        print("\n" + "=" * 50)
        print("        TOURISMPULSE - TRAVEL ANALYTICS ENGINE")
        print("        Understand destinations through data")
        print("=" * 50)

        print("\n1. Exploratory Tourism Analysis")
        print("2. Seasonal Visitor Analysis")
        print("3. Peak and Off-Peak Analysis")
        print("4. Visitor Preference Analysis")
        print("5. Tourist Demographic Analysis")
        print("6. Destination Popularity Scores")
        print("7. Future Tourist Demand Forecast")
        print("8. Destination Comparison")
        print("9. Emerging Tourist Hotspots")
        print("10. Generate Tourism Trend Report")
        print("11. Generate Visual Dashboard")
        print("0. Exit")

    def run(self):

        if self.logger:
            self.logger.info(
                "TourismPulse application started."
            )

        while True:

            self.display_menu()

            choice = input("\nEnter your choice: ")

            try:

                if choice == "1":
                    analyzer = TourismEDA(
                        self.tourism_file
                    )

                    analyzer.load_data()
                    analyzer.dataset_summary()
                    analyzer.tourist_summary()
                    analyzer.top_states()
                    analyzer.purpose_analysis()

                elif choice == "2":
                    analyzer = SeasonalAnalyzer(
                        self.tourism_file
                    )

                    analyzer.load_data()

                    seasonal_data = (
                        analyzer.analyze_seasonal_visitors()
                    )

                    analyzer.identify_popular_season(
                        seasonal_data
                    )

                    analyzer.analyze_seasonal_preferences()

                elif choice == "3":
                    analyzer = PeakOffPeakAnalyzer(
                        self.tourism_file
                    )

                    analyzer.load_data()

                    monthly_data = (
                        analyzer.analyze_monthly_visitors()
                    )

                    analyzer.identify_peak_offpeak(
                        monthly_data
                    )

                elif choice == "4":
                    analyzer = VisitorAnalyzer(
                        self.tourism_file
                    )

                    analyzer.load_data()

                    analyzer.analyze_visit_preferences()

                    analyzer.analyze_domestic_foreign_visitors()

                    analyzer.analyze_state_preferences()

                elif choice == "5":
                    analyzer = DemographicAnalyzer(
                        self.demographic_file
                    )

                    if analyzer.load_data():
                        analyzer.analyze_gender()
                        analyzer.analyze_age_groups()

                elif choice == "6":
                    analyzer = PopularityScoreAnalyzer(
                        self.tourism_file
                    )

                    analyzer.load_data()

                    popularity_data = (
                        analyzer.calculate_popularity_score()
                    )

                    analyzer.display_top_destinations(
                        popularity_data
                    )

                elif choice == "7":
                    analyzer = TourismDemandForecaster(
                        self.tourism_file
                    )

                    analyzer.load_data()

                    monthly_data = (
                        analyzer.prepare_monthly_data()
                    )

                    slope, intercept = (
                        analyzer.calculate_trend(
                            monthly_data
                        )
                    )

                    analyzer.forecast_future_demand(
                        monthly_data,
                        slope,
                        intercept
                    )

                elif choice == "8":
                    analyzer = DestinationComparator(
                        self.tourism_file
                    )

                    analyzer.load_data()

                    destination_data = (
                        analyzer.prepare_destination_data()
                    )

                    analyzer.compare_destinations(
                        destination_data
                    )

                    analyzer.top_destinations_by_parameter(
                        destination_data
                    )

                elif choice == "9":
                    analyzer = EmergingHotspotAnalyzer(
                        self.tourism_file
                    )

                    if analyzer.load_data():

                        hotspot_data = (
                            analyzer.analyze_destination_growth()
                        )

                        emerging_hotspots = (
                            analyzer.identify_emerging_hotspots(
                                hotspot_data
                            )
                        )

                        analyzer.display_top_hotspots(
                            emerging_hotspots
                        )

                elif choice == "10":
                    analyzer = TourismTrendReport(
                        self.tourism_file
                    )

                    if analyzer.load_data():

                        insights = analyzer.generate_insights()

                        analyzer.display_insights(
                            insights
                        )

                        analyzer.generate_report(
                            insights
                        )

                elif choice == "11":
                    dashboard = TourismDashboard(
                        self.tourism_file
                    )

                    if dashboard.load_data():
                        dashboard.generate_dashboard()

                elif choice == "0":
                    print(
                        "\nThank you for using TourismPulse."
                    )

                    if self.logger:
                        self.logger.info(
                            "TourismPulse application closed."
                        )

                    break

                else:
                    print(
                        "\nInvalid choice. Please try again."
                    )

            except Exception as error:

                print(
                    "\nApplication Error:",
                    error
                )

                if self.logger:
                    self.logger.exception(
                        "TourismPulse module error."
                    )


if __name__ == "__main__":

    application = TourismPulse()

    application.run()