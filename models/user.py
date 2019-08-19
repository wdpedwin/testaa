from models import db
from sqlalchemy import Column
from sqlalchemy import String,Integer

class User(db.Model):
    id = Column(Integer,
                primary_key=True,
                autoincrement=True)
    phone = Column(String(20),unique=True,
                  nullable=False)
    auth_key = Column(String(100),nullable=False)
    nick_name = Column(String(20))
    photo = Column(String(100))

