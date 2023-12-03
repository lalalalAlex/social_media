from fastapi import APIRouter, UploadFile
from user import LoginUserValidator, RegisterUserValidator, EditUserValidator
from database.userservice import register_user_db, login_user_db, add_profile_photo_db, delete_profile_photo_db, get_all_users_db, get_exact_user_db

user_router = APIRouter(prefix='/user', tags=['Пользователи и Настройки'])


@user_router.post('/login')
async def login_user(data: LoginUserValidator):
    result = login_user_db(**data.model_dump())

    return {'message': result}


@user_router.post('/register')
async def register_user(data: RegisterUserValidator):
    result = register_user_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Пользователь с такой почтой есть'}


@user_router.get('/get-user')
def get_user(user_id: int = 0):
    if user_id == 0:
        result = get_all_users_db()
        return {'message': result}
    else:
        result = get_exact_user_db(user_id)
        return {'message': result}
