from app.extensions.sqlalchemy import orm as DB
from .Person import Person


class User(Person):
    __tablename__ = "Users"
    weiht = DB.Column(DB.Numeric(), nullable=False)
    height = DB.Column(DB.Numeric(), nullable=False)
    
    def __repr__(self) -> str:
        return f"<User: {self.name}>"
