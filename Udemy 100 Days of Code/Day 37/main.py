import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = ""
USERNAME = "roysiu"
ID = "graph1"

todays_date = dt.datetime.now()
date = todays_date.strftime("%G%m%d")
print(date)
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create user
# response = requests.post(url = pixela_endpoint, json = pixela_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID,
    "name": "Coding Graph",
    "unit": "Commits",
    "type": "int",
    "color": "ajisai"
}

# authentication header instead of parsing through the API token.
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

pixel_config = {
    "date": date,
    "quantity": "1"
}

# response = requests.post(url = pixel_endpoint, json = pixel_config, headers = headers)
# print(response.text)

pixel_update = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{date}"
update_config = {
    "quantity": "5"
}

# response = requests.put(url = pixel_update, json = update_config, headers = headers)
# print(response.text)

# pixel_delete = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{date}"

# response = requests.delete(url = pixel_delete, headers = headers)