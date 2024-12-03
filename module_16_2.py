from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()


@app.get("/user/admin")
async def Get_Admin_Page():
    return 'Вы вошли как администратор'


@app.get("/user/{user_id}")
async def Get_User_Number(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User Id')]) -> str :
    return f'Вы вошли как пользователь № {user_id}'


@app.get("/user/{user_name}/{age}")
async def Get_User_Info(user_name: Annotated[str, Path(ge=5, le=20, description='Enter username', example='Ivan')],
                        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='55')])->str:
    return f'Информация о пользователе. Имя: {user_name}, Возраст: {age}'


@app.get("/")
async def Get_main_page():
    return 'Главная страница'

#                                                  python -m uvicorn module_16_1:app
