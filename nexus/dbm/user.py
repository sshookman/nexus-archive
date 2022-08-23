from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    pswd_hash = Column(String)

    def authenticate(self, password):
        return (str(hash(password)) == self.pswd_hash)

def create(engine):
    Base.metadata.create_all(engine)
