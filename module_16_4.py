"""Задача "Модель пользователя":"""

#               Подготовка:
#   Используйте CRUD запросы из предыдущей задачи.
#   Создайте пустой список users = []
#   Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
#       id - номер пользователя (int)
#       username - имя пользователя (str)
#       age - возраст пользователя (int)
#
#   Измените и дополните ранее описанные 4 CRUD запроса:

from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel, ConfigDict
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


# get запрос по маршруту '/users' теперь возвращает список users.

@app.get("/users")
async def get_users() -> list[User]:
    return users


#   post запрос по маршруту '/user/{username}/{age}', теперь:
#       Добавляет в список users объект User.
#       id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
#       Все остальные параметры объекта User - переданные в функцию username и age соответственно.
#       В конце возвращает созданного пользователя.

@app.post("/user/", response_model=User)
async def post_user(user: User) -> str:
    user.id = len(users) + 1
    users.append(user)
    return f"User {user.id} is registered"


#   put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
#       Обновляет username и age пользователя, если пользователь с таким user_id есть
#       в списке users и возвращает его.
#       В случае отсутствия пользователя выбрасывается исключение HTTPException с
#       описанием "User was not found" и кодом 404.

@app.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int, username: str = Body(), age: int = Body()) -> str:
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
        return f"The user {user_id} is registered"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


#   delete запрос по маршруту '/user/{user_id}', теперь:
#       Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
#       В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием
#       "User was not found" и кодом 404.

@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f"User with {user_id} was deleted."
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
