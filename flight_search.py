import requests

class FlightSearch:
    def __init__(self):
        pass

    def search_flights(self, city):
        api_end_point = "https://tequila-api.kiwi.com/locations/query"
        parameters = {
            "term": f"{city}"
        }
        header = {
            "apikey": "Iak0yghjoest46eSGnmoQaAJHFo5YNUN",
            "Content-Type": "application/json"
        }

        response = requests.get(url=api_end_point, params=parameters, headers=header)
        data = response.json()['locations'][0]["code"]
        return data