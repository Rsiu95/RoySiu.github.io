import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

QUESTION_API = requests.get(url = "https://opentdb.com/api.php", params = parameters)

data = QUESTION_API.json()

question_data = []

for question in data["results"]:
    question_data.append(question)
