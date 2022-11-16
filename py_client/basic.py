import requests

endpoint = "http://127.0.0.1:8000/api/"
get_respons = requests.get(endpoint, json={"product_id":12})
# print(get_respons.text)
print(get_respons.json())
print(get_respons.status_code)