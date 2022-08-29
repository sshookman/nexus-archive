import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from ...conf import VOYAGERS_DB
from .voyagerTable import Voyager, create_voyager_table

class VoyagerService:

    session = None

    def __init__(self, database=VOYAGERS_DB):
        # Establish connection the voyager database and create and missing tables
        engine = create_engine(f"sqlite:///{database}")
        create_voyager_table(engine)

        # Establish a Session with this database connection
        SessionMaker = sessionmaker()
        SessionMaker.configure(bind=engine)
        self.session = SessionMaker()

    def authenticate(self, username, password):
        voyager = self.get_voyager(username)
        return voyager.authenticate(password)

    def read(self, username):
        return self.session.query(Voyager).filter(Voyager.username == username).one_or_none()

    def create(self, username, password_text):
        try:
            password = bcrypt.hashpw(password_text.encode(), bcrypt.gensalt())
            voyager = Voyager(username=username, password=password)
            self.session.add(voyager)
            self.session.commit()
        except Exception as exc:
            print(f"Failed to Create New Voyager {exc}")
            self.session.rollback()

    #def read_all(self, page=0):
    #def update(self, username, password):
    #def delete(self, username, password):

    def close(self):
        self.session.close()
