import fastapi
from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/")
async def get_all_messages()  -> dict:
    pass

@app.get("/user/{user_id}")
async def kjh():
    pass


dict_ = {1: ("sdf", 99), 2: ('kjhkjh', 88)}

print(dict_("sdf"))

























# @app.get("/")                                                                  # Если мы получили Гет запрос такого типа, то отработай эту функцию
# async def welcome() -> dict:                                                   # Тут указываем какой тип данных функция возвращает (это не обязательно, но очень полезно)
#     return {"message": "Hello World"}                                               # И возвращаем мы словарик
#
# @app.get("/main")
# async def welcome() -> dict:
#     return {"message": "Main page"}                                                # Тут будет возвращать станицу "Main page"

# Get  - адрес в строке, это выглядит так -  ?переменная=значение. еще считаю что это получение данных С сервира, а Пост
# Post - формы - оформиить заказ в магазине (например). Еще считается что это отправка данных На сервер
# Put  - по своей сути пытается что то обновить, заменить и так далее
#Delete - удаляет

#  Что бы запрустить пишем с строке Терминала -      python3 -m uvicorn main:app
#                                                    python -m uvicorn main:app