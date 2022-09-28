import requests
import json


if __name__ == "__main__":
    payload = {
        "name": "User"        
    }
    
    response = requests.get(
        "https://playground.learnqa.ru/api/hello",
        params = payload
        )
    
    answer = json.loads(response.text)["answer"]

    print(answer)