import requests
import datetime

class FlightData:
    def __init__(self):
         pass

    def get_flight_prices(self, city, city_code, departure_city):
        six_months = datetime.datetime.now() + datetime.timedelta(180)
        six_months_time = six_months.date().strftime("%d/%m/%Y")
        tomorrow = datetime.datetime.now() + datetime.timedelta(1)
        tomorrow_date = tomorrow.date().strftime("%d/%m/%Y")
        api_end_point = "https://tequila-api.kiwi.com/v2/search"
        parameters = {
            "fly_from": f"{departure_city}",
            "fly_to": f"{city_code}",
            "date_from": f"{tomorrow_date}",
            "date_to": f"{six_months_time}"
        }
        header = {
            "apikey": "Iak0yghjoest46eSGnmoQaAJHFo5YNUN",
            "Content-Type": "application/json"
        }

        response = requests.get(url=api_end_point, params=parameters, headers=header)
        data = response.json()["data"][0]["price"]
        return data

