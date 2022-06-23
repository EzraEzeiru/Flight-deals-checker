from pprint import pprint
import requests
class DataManager:
    def __init__(self):
        self.sheet_endpoint = "https://api.sheety.co/06544ea584a763d682260465198ce764/copyOfFlightDeals/prices"

    def get_sheets(self):
        self.sheet_response = requests.get(url=self.sheet_endpoint)
        self.data = self.sheet_response.json()["prices"]
        return  self.data

    def update_entry(self, entry, id):
        update_sheet = {
            "price": {
                "iataCode": f"{entry}"
            }
        }
        sheety_header = {
            "Content-Type": "application/json"
        }
        put_end_point = f"https://api.sheety.co/06544ea584a763d682260465198ce764/copyOfFlightDeals/prices/{id}"
        put_response = requests.put(url=put_end_point, json=update_sheet, headers=sheety_header)

        print("It was successful")
