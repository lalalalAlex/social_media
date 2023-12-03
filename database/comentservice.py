from .models import Comment
from database import get_db


def add_comment_db(user_id, post_id, comment_text):
    db = next(get_db())
    new_comment = Comment(user_id=user_id, post_id=post_id, comment_text=comment_text)
    db.add(new_comment)
    db.commit()

    return 'Комментарий успешно добавлен'


def edit_comment_db(new_comment, comment_id):
    db = next(get_db())
    edit_comment = db.query(Comment).filter_by(id=comment_id).first()
    if edit_comment:
        edit_comment.comment_text = new_comment
        db.commit()
        print = {'Комментарий успешно изменен на': new_comment}

        return print
    else:
        return False


def delete_comment_db(comment_id):
    db = next(get_db())
    delete_comment = db.query(Comment).filter_by(id=comment_id).first()
    if delete_comment:
        db.delete(delete_comment)
        return 'Комментарий успешно удален'
    else:
        return False


def exact_post_comments(post_id):
    db = next(get_db())
    exact_comment = db.query(Comment).filter_by(post_id=post_id).first()

    if exact_comment:
        return exact_comment
    else:
        return 'Коментариев пока что нет'

