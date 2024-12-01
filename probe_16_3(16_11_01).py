from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/")
async def get_all_messages() -> dict:
    return users

# @app.get("/user/{user_id}")
# async def

# Get  - адрес в строке, это выглядит так -  ?переменная=значение. еще считаю что это получение данных С сервира
# Post - формы - оформиить заказ в магазине (например). Еще считается что это отправка данных На сервер
# Put  - по своей сути пытается что то обновить, заменить и так далее
# Delete - удаляет




#                                                  python -m uvicorn probe_16_3(16_11_01):app