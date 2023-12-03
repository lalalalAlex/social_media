from fastapi import APIRouter, UploadFile, Body
from post import AddPostValidator, EditPostValidator
from database.postservice import add_post_db, add_post_photo_db, edit_post_db, delete_post_db, get_exact_post_db, get_all_posts_db


post_router = APIRouter(prefix='/post', tags=['Посты и Настройки'])


@post_router.post('/add-post')
async def add_post(data: AddPostValidator):
    result = add_post_db(**data.model_dump())
    return {'messge': result}


@post_router.put('/edit-post')
async def edit_posts(data: EditPostValidator):
    result = edit_post_db(**data.model_dump())
    if result:
        return {'messge': result}
    else:
        return {'message': 'Пост не изменен. Ошибка'}


@post_router.delete('/delete-post')
async def login_user(post_id: int):
    result = delete_post_db(post_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'Пост не удален. Ошибка'}


@post_router.get('/get-posts')
async def all_posts():
    result = get_all_posts_db()
    if result:
        return {'message': result}
    else:
        return {'message': 'Постов пока что нет'}


@post_router.post('/add-photo-post')
async def add_photo_post(post_id: int = Body(), user_id: int = Body(), photo_file: UploadFile = None):
    photo_path = f'/media/{photo_file.filename}'
    try:
        with open (f'media/{photo_file.filename}', 'wb') as file:
            user_photo = await photo_file.read()
            file.write(user_photo)
            result = add_post_photo_db(post_id=post_id, post_photo=photo_path)
    except Exception as error:
        result = error
        return {'message': result}
    return {'message': result}


@post_router.get('/get-exact-post')
async def get_exact_post(post_id: int):
    result = get_exact_post_db(post_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'Такого поста нет. Ошибка'}



