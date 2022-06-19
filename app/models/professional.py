from app.extensions.sqlalchemy import orm as DB
from .Person import Person


class Professional(Person):
    __tablename__ = "Professional"
    profession = DB.Column(DB.String(50), nullable=False)
    
    def __repr__(self) -> str:
        return f"<Professional: {self.name}>"
