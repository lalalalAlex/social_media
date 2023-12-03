from fastapi import APIRouter, UploadFile, File
from database.postservice import add_post_db, add_post_photo_db, edit_post_db, delete_post_db, get_exact_post_db, get_all_posts_db
from datetime import datetime

post_router = APIRouter(prefix='/post', tags=['Посты'])


@post_router.post('/add_post')
async def add_post(user_id: int, post_text: str):
    post = add_post_db(user_id, post_text)

    return post


@post_router.post('/add_post_photo')
async def add_photo(post_id: int, post_photo: UploadFile):
    with open(f'media/{post_photo.filename}', 'wb') as file:
        front_photo = await post_photo.read()
        file.write(front_photo)

    photo = add_post_photo_db(f'/media/{post_photo.filename}', post_id)

    return photo


@post_router.post('/edit_post')
async def edit_post(user_id: int, new_text: str, post_id: int):
    post = edit_post_db(user_id, post_id, new_text)

    return post


@post_router.post('/delete_post')
async def delete_post(post_id: int):
    post = delete_post_db(post_id)

    return post


@post_router.post('/all_posts')
async def get_all_post():
    post = get_all_posts_db()

    return post


@post_router.post('/exact_post')
async def exact_post(post_id: int):
    post = get_exact_post_db(post_id)

    return post