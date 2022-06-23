from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_sheets()
DEPARTURE_CITY = "London"
DEPARTURE_CITY_IATA = "LON"
print(sheet_data)
id = 2

if sheet_data[0]["iataCode"] == "":
   for data in sheet_data:
      city_name = data["city"]
      flight = FlightSearch()
      flight_result = flight.search_flights(city_name)
      data_manager.update_entry(flight_result, id)
      id += 1


for data in sheet_data:
   city_name = data["city"]
   city_code = data["iataCode"]
   new_flight_data = FlightData()
   flight_price = new_flight_data.get_flight_prices(city_name, city_code, DEPARTURE_CITY_IATA)
   if flight_price < data["lowestPrice"]:
      send_notification = NotificationManager()
      message = f"Low Price Alert! Only ${flight_price} to fly from {DEPARTURE_CITY} to {city_name}"
      send_notification.send_sms(message)


