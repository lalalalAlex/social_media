from pydantic import BaseModel


class AddPostValidator(BaseModel):
    user_id: int
    post_text: str


class EditPostValidator(BaseModel):
    user_id: int
    new_text: str
    post_id: int


class DeletePostValidator(BaseModel):
    post_id: int


class ExactPostValidator(BaseModel):
    post_id: int

