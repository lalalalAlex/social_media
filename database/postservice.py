from .models import UserPost, PostPhoto
from datetime import datetime
from database import get_db


def add_post_db(user_id: int, post_text: str) -> object:
    db = next(get_db())
    new_post = UserPost(user_id=user_id, post_text=post_text, publish_date=datetime.now())
    db.add(new_post)
    db.commit()

    return f'Пост успешно добавлен'


def add_post_photo_db(post_id, post_photo):
    db = next(get_db())
    new_post_photo = PostPhoto(post_id=post_id, post_photo=post_photo)
    db.add(new_post_photo)
    db.commit()

    return 'Фото поста успешно изменено'


def edit_post_db(post_id, user_id, new_text):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(id=post_id, user_id=user_id).first()
    if exact_post:
        exact_post.post_text = new_text
        db.commit()
        print = {'Текст': exact_post.post_text,
                 'Время публикации': exact_post.publish_date}

        return print
    else:
        return False


def delete_post_db(post_id: int):
    db = next(get_db())
    delete_post = db.query(UserPost).filter_by(id=post_id).first()
    delete_post_photo = db.query(UserPost).filter_by(id=post_id).first()
    if delete_post:
        db.delete(delete_post)
        db.delete(delete_post_photo)
        db.commit()
        return 'Пост успешно удален'
    else:
        return 'Ошибка, пост был не найден'


def get_all_posts_db():
    db = next(get_db())
    all_posts = db.query(UserPost).all()
    return all_posts


def get_exact_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(id=post_id).first()
    return exact_post

