import datetime

date = datetime.date.today()
DATE_FROM = (date + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
DATE_TO = (date + datetime.timedelta(days=181)).strftime("%d/%m/%Y")


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(
        self,
        price,
        origin_city,
        origin_airport,
        destination_city,
        destination_airport,
        flight_date,
        return_flight_date,
        deep_link,
        stop_overs=0,
        via_city="",
    ):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airpot = destination_airport
        self.flight_date = flight_date
        self.return_flight_date = return_flight_date
        self.deep_link = deep_link
        self.stop_overs = stop_overs
        self.via_city = via_city
