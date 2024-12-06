from fastapi import FastAPI, Path, status, Body, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                   age: Annotated[int, Path(ge=18, le=120, description="Enter age")]) -> User:
    if len(users) >= 1:
        user_id = users[-1].id + 1
    else:
        user_id = 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')], username: Annotated[str,
Path(min_length=5, max_length=20, description='Enter username')], age: Annotated[int,
Path(ge=18, le=120, description='Enter age')]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    else:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id):
    for user in users:
        if user_id == user_id:
            users.pop(int(user_id))
            return user_id
    else:
        raise HTTPException(status_code=404, detail='User was not found')

#                                                                               python -m uvicorn module_16_4:app


# Get  - адрес в строке, это выглядит так -  ?переменная=значение. еще считаю что это получение данных С сервира
# Post - формы - оформиить заказ в магазине (например). Еще считается что это отправка данных На сервер
# Put  - по своей сути пытается что то обновить, заменить и так далее
# Delete - удаляет
