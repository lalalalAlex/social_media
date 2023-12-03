from fastapi import APIRouter, UploadFile, File
from database.userservice import register_user_db, login_user_db, add_profile_photo_db, delete_profile_photo_db, get_all_users_db, get_exact_user_db

user_router = APIRouter(prefix='/user', tags=['Пользователи'])


@user_router.post('/register')
async def register(name: str, surname: str, email: str, phone_number: str, city: str, password: str):
    reg = register_user_db(name, surname, email, phone_number, city, password)

    return reg


@user_router.post('/login')
async def login_user(email: str, password: str):
    log = login_user_db(email, password)

    return log


@user_router.post('/add_profile_photo')
async def profile_photo_user(user_id: int, profile_photo: UploadFile):
    with open(f'media/{profile_photo.filename}', 'wb') as file:
        front_photo = await profile_photo.read()
        file.write(front_photo)

    photo = add_profile_photo_db(f'/media/{profile_photo.filename}', user_id)

    return photo


@user_router.post('/delete_profile_photo')
async def profile_photo_user(user_id: str):
    photo = delete_profile_photo_db(user_id)

    return photo


@user_router.post('/all_users')
async def all_users():
    users = get_all_users_db()

    return users


@user_router.post('/exact_user')
async def user(user_id: str):
    exact_user = get_exact_user_db(user_id)

    return exact_user
