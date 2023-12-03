from pydantic import BaseModel


class AddCommentValidator(BaseModel):
    user_id: int
    post_id: int
    comment_text: str


class EditCommentValidator(BaseModel):
    new_comment: str
    comment_id: int


class ExactCommentValidator(BaseModel):
    post_id: int
