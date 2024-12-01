from fastapi import FastAPI, Path, status, Body, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int =None
    username: str
    age: int


@app.get("/users")
async def get_all_messages() -> list[User]:
    return users


@app.post("/user/{username}/{age}")
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                   age: Annotated[int, Path(ge=18, le=120, description="Enter age")]) -> User:
    if len(users) >= 1:
        user_id = len(users) + 1
    else:
        user_id = 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id=int, username=str, age=int) -> str:
    users[user_id] = f'{username}, {age}'
    return f"The user {user_id} is updated"


@app.delete('/user/{user_id}')
async def delete_user(user_id):
    users.pop(user_id)

#                                                  python -m uvicorn module_16_4:app


# Get  - адрес в строке, это выглядит так -  ?переменная=значение. еще считаю что это получение данных С сервира
# Post - формы - оформиить заказ в магазине (например). Еще считается что это отправка данных На сервер
# Put  - по своей сути пытается что то обновить, заменить и так далее
# Delete - удаляет
