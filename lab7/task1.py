import requests

city = "Helsinki"
api_key = "3358f3fac7b54eb314527d243263874f"
url = "https://api.openweathermap.org/data/2.5/weather"

# выбираем параметры: город, ключ, метрическая система, русский язык
params = {
    "q": city,
    "appid": api_key,
    "units": "metric",
    "lang": "ru"
}

response = requests.get(url, params=params)  # отправляем get-запрос по нашим параметрам
data = response.json()  # превращаем ответ сэрвера в словарь

temp = data['main']['temp']
humidity = data['main']['humidity']
pressure = data['main']['pressure']

print(f"Город: {city}")
print(f"Температура: {temp}°C")
print(f"Влажность: {humidity}%")
print(f"Давление: {pressure} hPa")
