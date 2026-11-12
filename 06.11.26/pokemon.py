import requests

URL = "https://pokeapi.co/api/v2"


def main():
    response = requests.get(URL + "/pokemon?limit=20")
    data = response.json()

    names = [pokemon["name"] for pokemon in data["results"]]

    print("Первые 20 покемонов:")
    for name in names:
        print("-", name)

    name = input("\nИмя покемона: ").strip().lower()

    response = requests.get(URL + "/pokemon/" + name)
    if response.status_code != 200:
        print("Покемон не найден или ошибка запроса:", response.status_code)
        return

    pokemon = response.json()

    types = [t["type"]["name"] for t in pokemon["types"]]
    abilities = [a["ability"]["name"] for a in pokemon["abilities"]]

    print("\nИмя:", pokemon["name"])
    print("Тип:", ", ".join(types))
    print("Вес:", pokemon["weight"] / 10, "кг")
    print("Рост:", pokemon["height"] / 10, "м")
    print("Способности:", ", ".join(abilities))


main()
