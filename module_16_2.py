from fastapi import FastAPI

app = FastAPI()


@app.get("/user/admin")
async def Get_Admin_Page():
    return 'Вы вошли как администратор'


@app.get("/user/{user_id}")
async def Get_User_Number(user_id: str, ):
    return f'Вы вошли как пользователь № {user_id}'


@app.get("/user/{user_name}/{age}")
async def Get_User_Info(user_name: str, age=int):
    return f'Информация о пользователе. Имя: {user_name}, Возраст: {age}'


@app.get("/")
async def Get_main_page():
    return 'Главная страница'

#                                                  python -m uvicorn module_16_1:app
