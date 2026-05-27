import httpx
from typing import Dict, Any

with httpx.Client(base_url='https://jsonplaceholder.typicode.com') as client:

    response = client.get('/todos/1')

    print("===GET запрос===")
    print(f"Response код: {response.status_code}")
    print(f"Данные: {response.json()}")
    print(f"Время выполнения: {response.elapsed}")

    print("*" * 45)

    data = {
        "userId": 1,
        "title": "Новая задача",
        "completed": False
    }

    response = client.post('/todos', json=data)

    print("===POST запрос===")
    print(f"Response код: {response.status_code}")
    print(f"Данные: {response.json()}")
    print(f"Время выполнения: {response.elapsed}")

    print("*" * 45)


    params: Dict[str, Any] = {"userId": 1}
    response = client.get("/todos", params=params)

    print("===GET запрос===")
    print(f"URL: {response.url}")
    print(f"Response код: {response.status_code}")
    print(f"Данные: {response.json()}")
    print(f"Время выполнения: {response.elapsed}")

    print("*" * 45)

    try:
        response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
        response.raise_for_status()  # Вызовет исключение при 4xx/5xx
    except httpx.HTTPStatusError as e:
        print(f"Ошибка запроса: {e}")

# with httpx.Client(base_url='https://httpbin.org') as client_2:
#     headers = {"Authorization": "Bearer my_secret_token"}
#     response = client_2.get('/get', headers= headers)
#
#
#     print("===POST запрос===")
#     print(f"Заголовки: {response.request.headers}")
#     print(f"Response код: {response.status_code}")
#     print(f"Данные: {response.json()}")
#     print(f"Время выполнения: {response.elapsed}")
#
#     print("*" * 45)