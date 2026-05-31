import httpx
from tools import fakers

with httpx.Client(base_url="http://127.0.0.1:8000") as client:

    #===================================
    # Создание пользователя
    # ===================================

    email = fakers.get_random_email()
    password = "12345678"

    create_user_payload = {
            "email": email,
            "password": password,
            "lastName": "string",
            "firstName": "string",
            "middleName": "string"
        }

    create_user_response = client.post("/api/v1/users", json = create_user_payload)

    print("===Создаём пользователя===")

    create_user_response_data = create_user_response.json()
    print(f"Пользователь создан: {create_user_response_data}")
    print(f"Время использования: {create_user_response.elapsed}")

    # ===================================
    # Логин
    # ===================================

    login_payload = {
        "email": create_user_payload["email"],
        "password": create_user_payload["password"]
    }

    login_response = client.post("/api/v1/authentication/login", json=login_payload)

    login_response_data = login_response.json()
    print(f"Login data: {login_response_data}")
    print(f"Время использования: {login_response.elapsed}")


    # ===================================
    # Удаление пользователя
    # ===================================

    delete_user_headers = {
        "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
    }

    delete_user_response = client.delete(f'/api/v1/users/{create_user_response_data['user']['id']}',
                                         headers= delete_user_headers
                                         )

    print(f"Delete data: {delete_user_response.status_code}")
    print(f"Время использования: {delete_user_response.elapsed}")
