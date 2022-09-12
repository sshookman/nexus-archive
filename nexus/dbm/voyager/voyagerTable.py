import bcrypt
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Voyager(Base):
    __tablename__ = "voyager"
    voyager_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def authenticate(self, password_text):
        return bcrypt.checkpw(password_text.encode(), self.password)

def create_voyager_table(engine):
    Base.metadata.create_all(engine)
