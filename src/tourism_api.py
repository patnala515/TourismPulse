import requests
import json
import os


class TourismAPI:

    def __init__(self):
        self.base_url = "https://nominatim.openstreetmap.org/search"
        self.output_folder = "data/api"

    def fetch_destination_data(self, destination):
        try:
            params = {
                "q": f"{destination}, India",
                "format": "json",
                "limit": 1,
                "countrycodes": "in"
            }

            headers = {
                "User-Agent": "TourismPulse-College-Project"
            }

            response = requests.get(
                self.base_url,
                params=params,
                headers=headers,
                timeout=10
            )

            response.raise_for_status()

            results = response.json()

            if not results:
                print("Indian destination not found.")
                return None

            print("Indian destination data fetched successfully.")

            return results[0]

        except requests.RequestException as error:
            print("API Error:", error)
            return None

    def display_destination_data(self, destination):
        print("\nDestination Information:")
        print(f"Name: {destination.get('display_name')}")
        print(f"Latitude: {destination.get('lat')}")
        print(f"Longitude: {destination.get('lon')}")

    def save_json_data(self, destination):
        os.makedirs(self.output_folder, exist_ok=True)

        file_path = (
            f"{self.output_folder}/destination_data.json"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as json_file:
            json.dump(
                destination,
                json_file,
                indent=4
            )

        print("\nAPI data saved successfully.")
        print(f"JSON file saved at: {file_path}")


if __name__ == "__main__":

    api = TourismAPI()

    destination_name = input(
        "Enter Indian tourist destination or state: "
    )

    destination_data = api.fetch_destination_data(
        destination_name
    )

    if destination_data:
        api.display_destination_data(destination_data)
        api.save_json_data(destination_data)