import requests
import json


if __name__ == "__main__":
    response = requests.get(
        "https://playground.learnqa.ru/api/hello"
        )
    print(response.status_code)
    
    response = requests.get(
        "https://playground.learnqa.ru/api/get_404"
        )
    print(response.status_code)
    
    response = requests.get(
        "https://playground.learnqa.ru/api/get_500"
        )
    print(response.status_code)