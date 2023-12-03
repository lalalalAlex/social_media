from fastapi import FastAPI

from user.userapi import user_router
from post.postapi import post_router
from comment.commentapi import comment_router
from photo.photoapi import photo_router

# from user.user_api import user_router
# from post.post_api import post_router
# from comment.comment_api import comment_router

from database import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI(docs_url='/')
# app.include_router(user_router)
# app.include_router(post_router)
# app.include_router(comment_router)
app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)
app.include_router(photo_router)


@app.get('/home')
async def home_page():
    return 'Test page'


# @app.post('/add-post-db')
# async def add_post_db_route(user_id: int, post_text: str):
#     return add_post_db(user_id, post_text)
