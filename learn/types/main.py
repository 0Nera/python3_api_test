import requests
import json


if __name__ == "__main__":
    response = requests.get(
        "https://playground.learnqa.ru/api/check_type",
        params={"Hello": "World"}
        )
    print(response.text)

    response = requests.post(
        "https://playground.learnqa.ru/api/check_type",
        data= {"Python": 3}
        )
    print(response.text)

    response = requests.put(
        "https://playground.learnqa.ru/api/check_type",
        data= {"ping": "pong"}
        )
    print(response.text)

    response = requests.delete(
        "https://playground.learnqa.ru/api/check_type",
        data= {"cup": "tea"}
        )
    print(response.text)