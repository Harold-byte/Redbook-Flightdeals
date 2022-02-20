import os
import requests

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_TOKEN = os.environ['SHEETY_TOKEN']
SHEETY_HEADERS = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=SHEETY_HEADERS
            )
            print(response.text)
