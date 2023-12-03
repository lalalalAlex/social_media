from fastapi import APIRouter, UploadFile
from comment import AddCommentValidator, EditCommentValidator, ExactCommentValidator
from database.comentservice import add_comment_db, edit_comment_db, delete_comment_db, exact_post_comments


comment_router = APIRouter(prefix='/comment', tags=['Комментарии и Настройки'])


@comment_router.post('/add-comment')
async def add_comments(data: AddCommentValidator):
    result = add_comment_db(**data.model_dump())

    return {'message': result}


@comment_router.put('/edit-comment')
async def edit_comments(data: EditCommentValidator):
    result = edit_comment_db(**data.model_dump())

    return {'message': result}


@comment_router.post('/exact-post-comment')
async def exact_comments(data: ExactCommentValidator):
    result = exact_post_comments(**data.model_dump())

    return {'message': result}


@comment_router.delete('/delete-comment')
async def delete_comment(comment_id: int):
    result = delete_comment_db(comment_id)

    return {'message': result}
