from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def get_main_page() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def get_admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}

#   Допишите валидацию для маршрутов из предыдущей задачи при помощи классов Path и Annotated:
#   '/user/{user_id}' - функция, выполняемая по этому маршруту, принимает аргумент user_id,
#   для которого необходимо написать следующую валидацию:

#   1. Должно быть целым числом
#   2. Ограничено по значению: больше или равно 1 и меньше либо равно 100.
#   3. Описание - 'Enter User ID'
#   4. Пример - '1' (можете подставить свой пример не противоречащий валидации)

@app.get("/user/{user_id}")
async def get_user_number(user_id: int = Path(ge=1, le=100, description="Enter User ID", example="1")) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


#   '/user' замените на '/user/{username}/{age}' - функция, выполняемая по этому маршруту,
#   принимает аргументы username и age, для которых необходимо написать следующую валидацию:

#   1. username - строка, age - целое число.
#   2. username ограничение по длине: больше или равно 5 и меньше либо равно 20.
#   3. age ограничение по значению: больше или равно 18 и меньше либо равно 120.
#   4. Описания для username и age - 'Enter username' и 'Enter age' соответственно.
#   5. Примеры для username и age - 'UrbanUser' и '24' соответственно.
#   (можете подставить свои примеры не противоречащие валидации).

# @app.get("/user")
# async def get_user_info(username: str, age: int) -> dict:
#     return {"Информация о пользователе. Имя": username, "Возраст:": age}

@app.get('/user/{username}/{age}')
async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter Username", example="UrbanUser")],
                        age: int = Path(ge=18, le=120, description="Enter Age", example="24")) -> dict:
    return {"Информация о пользователе. Имя": username, "Возраст:": age}