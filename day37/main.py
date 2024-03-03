import requests
from datetime import datetime

USERNAME = "mlr990"
TOKEN = "PIXELA TOKEN"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
#
# graph_params = {
#     "id": "graph1",
#     "name": "Python Learning Graph",
#     "unit": "minutes",
#     "type": "int",
#     "color": "ajisai"
# }
#
headers = {
    "X-USER-TOKEN": TOKEN
}
# graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(graph_response.text)

# PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"
#
today = datetime.now().strftime("%Y%m%d")
#
# pixel_parameters = {
#     "date": today,
#     "quantity": "40"
# }
#
# pixel_response = requests.post(url=PIXEL_ENDPOINT, json=pixel_parameters, headers=headers)
# print(pixel_response.text)

# UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{today}"
#
# new_pixel_data = {
#     "quantity": "35"
# }
# update_response = requests.put(url=UPDATE_ENDPOINT, json=new_pixel_data, headers=headers)
# print(update_response.text)

DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{today}"


delete_response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
print(delete_response.text)
