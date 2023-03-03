from environment_variables import TEQUILA_API_KEY
from flight_data import FlightData

import requests
import datetime

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_HEADERS = {"apikey": TEQUILA_API_KEY, "accept": "application/json"}

date = datetime.date.today()
DATE_FROM = (date + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
DATE_TO = (date + datetime.timedelta(days=181)).strftime("%d/%m/%Y")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        PARAMS = {
            "term": city_name,
            "location_types": "airport",
        }
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/locations/query",
            params=PARAMS,
            headers=TEQUILA_HEADERS,
        )
        response.raise_for_status()
        data = response.json()["locations"]

        code = data[0]["code"]
        return code

    def check_flights(self, origin_city, destination_city):
        PARAMS = {
            "fly_from": origin_city,
            "fly_to": destination_city,
            "date_from": DATE_FROM,
            "date_to": DATE_TO,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD",
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            params=PARAMS,
            headers=TEQUILA_HEADERS,
        )

        response.raise_for_status()

        try:
            data = response.json()["data"][0]
            # pprint(data)

        except IndexError:
            PARAMS["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                params=PARAMS,
                headers=TEQUILA_HEADERS,
            )
            try:
                data = response.json()["data"][0]
            except IndexError:
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    flight_date=data["route"][0]["local_departure"].split("T")[0],
                    return_flight_date=data["route"][1]["local_departure"].split("T")[
                        0
                    ],
                    deep_link=data["deep_link"],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"],
                )
                return flight_data

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                flight_date=data["route"][0]["local_departure"].split("T")[0],
                return_flight_date=data["route"][1]["local_departure"].split("T")[0],
                deep_link=data["deep_link"],
            )
            return flight_data
