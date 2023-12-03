from fastapi import APIRouter, UploadFile, File
from database.comentservice import add_comment_db, edit_comment_db, delete_comment_db, exact_post_comments
from datetime import datetime

comment_router = APIRouter(prefix='/comment', tags=['Комментарии'])


@comment_router.post('/add_comment')
async def add_comments(user_id: int, post_id: int, comment_text: str):
    add = add_comment_db(user_id, post_id, comment_text)

    return add


@comment_router.post('/edit_comment')
async def edit_comments(new_comment: str, comment_id: int):
    edit = edit_comment_db(new_comment, comment_id)

    return edit


@comment_router.post('/delete_comment')
async def delete_comments(comment_id: int):
    delete = delete_comment_db(comment_id)

    return delete


@comment_router.post('/exact_post_comments')
async def exact_post_comments(post_id: int):
    exact = exact_post_comments(post_id)

    return exact
