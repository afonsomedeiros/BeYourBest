from app.extensions.sqlalchemy import orm as DB
from passlib.hash import pbkdf2_sha512 as sha
from datetime import datetime


class Professional(DB.Model):
    __tablename__ = "Professional"
    id = DB.Column("id", DB.Integer, primary_key=True)
    name = DB.Column(DB.String(50), nullable=False)
    email = DB.Column(DB.String(120), nullable=False)
    password = DB.Column(DB.String(200), nullable=False)
    profession = DB.Column(DB.String(50), nullable=False)
    created_at = DB.Column("created_at", DB.DateTime, default=datetime.utcnow)
    updated_at = DB.Column("updated_at", DB.DateTime, onupdate=datetime.utcnow)
    def __repr__(self) -> str:
        return f"<Professional: {self.name}>"

    def gen_hash(self):
        self.password = sha.hash(self.password)

    def verify(self, password):
        return sha.verify(password, self.password)