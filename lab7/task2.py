import requests

url = "https://rickandmortyapi.com/api/character"

params = {
    "status": "alive",
    "species": "human"
}


response = requests.get(url, params=params)  # Отправляем запрос по параметрам, далее переведем в формат JSON
data = response.json()

# Берём первые 5 персонажей из списка результатов
characters = data["results"][:5]

for person in characters:
    print(f"Имя: {person['name']}")
    print(f"Статус: {person['status']}")
    print(f"Раса: {person['species']}")
    print(f"Пол: {person['gender']}")
    print(f"Родная планета: {person['origin']['name']}")
    print(f"Текущая локация: {person['location']['name']}")
    print()
