import httpx
from tools.fakers import get_random_email

with httpx.Client(base_url='http://127.0.0.1:8000') as client:

    mainMail = get_random_email()
    password = '12345'

    #=============================
    # Создаем пользователя
    # =============================

    user_create = {
        "email": mainMail,
        "password": password,
        "lastName": "Ra",
        "firstName": "Sergey",
        "middleName": "St"
    }

    user = client.post('/api/v1/users', json=user_create)

    print("📥===POST запрос===📥")
    print(f"✳Респонс: {user.status_code}")
    print(f"✅Данные: {user.json()}")
    print(f"⚠Хедеры: {user.headers}")
    print(f"🕒Время выполнения: {user.elapsed}")


    # =============================
    # Аутентификация пользователя
    # =============================

    payload = {
        "email": mainMail,
        "password": password
    }
    response = client.post('/api/v1/authentication/login', json=payload)

    print("📥===POST запрос===📥")
    print(f"✳Респонс: {response.status_code}")
    print(f"✅Данные: {response.json()}")
    print(f"⚠Хедеры: {response.headers}")
    print(f"🕒Время выполнения: {response.elapsed}")


    # =============================
    # Получаем refreshToken
    # =============================
    refreshToken = {"refreshToken": response.json()['token']['refreshToken']}


    # =============================
    # Используем refreshToken
    # =============================
    get_refreshToken = client.post('/api/v1/authentication/refresh', json=refreshToken)

    print("📥===POST запрос===📥")
    print(f"✳Респонс: {get_refreshToken.status_code}")
    print(f"✅Данные: {get_refreshToken.json()}")
    print(f"⚠Хедеры: {get_refreshToken.headers}")
    print(f"🕒Время выполнения: {get_refreshToken.elapsed}")
