from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_all_messages() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def add_user(username=str, age=int) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, {age}'
    return f"User {current_index} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id, username, age) -> str:
    users[user_id] = f'{username}, возраст: {age}'
    return f"The user {user_id} is updated"


@app.delete('/user/{user_id}')
async def delete_user(user_id):
    users.pop(user_id)

#                                                  python -m uvicorn module_16_3:app


# Get  - адрес в строке, это выглядит так -  ?переменная=значение. еще считаю что это получение данных С сервира
# Post - формы - оформиить заказ в магазине (например). Еще считается что это отправка данных На сервер
# Put  - по своей сути пытается что то обновить, заменить и так далее
# Delete - удаляет
