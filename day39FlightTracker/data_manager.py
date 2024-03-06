import requests

SHEETY_ENDPOINT = "https://api.sheety.co/93f6a32d557e8d76b64477949daf9136/flightDeals/prices"
SHEETY_USER_ENDPOINT = "https://api.sheety.co/93f6a32d557e8d76b64477949daf9136/flightDeals/users"

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
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
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USER_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

