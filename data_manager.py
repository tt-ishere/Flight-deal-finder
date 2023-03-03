import requests

SHEETY_ENDPOINT_PRICES = (
    "https://api.sheety.co/6f2a55e1bb6e99174d7e1eb8e69e3b29/flightDeals/prices"
)

SHEETY_ENDPOINT_USERS = (
    "https://api.sheety.co/6f2a55e1bb6e99174d7e1eb8e69e3b29/flightDeals/users"
)


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.user_data = ""

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT_PRICES)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_ENDPOINT_PRICES}/{city['id']}", json=new_data
            )
            print(response.text)

    def get_user_data(self):
        user_response = requests.get(SHEETY_ENDPOINT_USERS)
        user_data = user_response.json()
        self.user_data = user_data["users"]
        return self.user_data
