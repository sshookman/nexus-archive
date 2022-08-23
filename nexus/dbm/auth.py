from ,user import User

class AuthService:

    session = None

    def __init__(self, database="archive/auth.sqlite"):
        # Establish connection the auth database file and create and missing tables
        engine = create_engine(f"sqlite:///{database}")
        User.create(engine)

        # Establish a Session with this database connection
        SessionMaker = sessionmaker()
        SessionMaker.configure(bind=engine)
        self.session = SessionMaker()

    def get_user(username):
        return self.session.query(User).filter(User.username == username).one_or_none()

    def add_user(username, password):
        user = User(username=username, pswd_hash=str(hash(password)))
        self.session.add(user)
        self.session.commit()

    def close():
        self.session.close()
