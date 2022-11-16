import requests

endpoint = "http://127.0.0.1:8000/api/"
get_respons = requests.get(endpoint, json={"query":"Hello World"})
# print(get_respons.text)
print(get_respons.json()['message'])
print(get_respons.status_code)