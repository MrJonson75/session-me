"""     Задача "Имитация работы с БД":
"""
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

#   Создайте новое приложение FastAPI и сделайте CRUD запросы.
#   Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}

users = {'1': 'Имя: Example, возраст: 18'}


#       Реализуйте 4 CRUD запроса:
#   1. get запрос по маршруту '/users', который возвращает словарь users.
#   2. post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по
#   максимальному по значению ключом значение строки "Имя: {username}, возраст: {age}".
#   И возвращает строку "User <user_id> is registered".
#   3. put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение
#   из словаря users под ключом user_id на строку "Имя: {username}, возраст: {age}".
#   И возвращает строку "The user <user_id> is registered"
#   4. delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users
#   по ключу user_id пару.

@app.get("/users")
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def post_user(
        username: Annotated[str, Path(min_length=6, max_length=12, description="Enter your name", example="Mikolo")],
        age: int = Path(ge=18, le=120, description="Enter your Age", example="36")) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    user_info = f"Имя: {username}, возраст: {age}"
    users[user_id] = user_info
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=0, le=100, description="Enter your user Id", example="2")]
                      , username: Annotated[
            str, Path(min_length=6, max_length=12, description="Enter new your name", example="Petro")]
                      , age: int = Path(ge=18, le=120, description="Enter new your Age", example="48")) -> str:
    user_info = f"Имя: {username}, возраст: {age}"
    users[str(user_id)] = user_info
    return f"The user {user_id} is registered"


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=0, le=100, description="Enter your user Id", example="2")]) -> str:
    users.pop(str(user_id))
    return f"User with {user_id} was deleted."
