import requests


api_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("City? ")

params = {
    'q': city,
    'appid': '665817c520f2d870db7eaae5e54baf6b',
    'units': 'metric',
}

res = requests.get(api_url, params=params)
# print(res.status_code)
# print(res.headers["Content-Type"])
# print(res.json())


data = res.json()
template = 'Current temperature in {} is {}'
print(template.format(city, data["main"]["temp"]))
//выключи микрофон
там внизу кнопк