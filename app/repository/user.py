from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
# from schematic import UserOut
# Create a connection to the Postgres database

engine = create_engine('postgresql://postgres:postgres@0.0.0.0:5432/')

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Define a User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    userName = Column(String)
    email = Column(String)
    profileUrl = Column(String, unique=True)
    profileSlug = Column(String, unique=True)
    password = Column(String)

# Create the users table in the database
Base.metadata.create_all(engine)



def create_user(username: str, email: str, profileurl: str, profileslug: str, password: str) -> bool:
    try:
        user = User(userName=username, email=email, profileUrl=profileurl, profileSlug=profileslug, password=password)
        session = Session()
        session.add(user)
        session.commit()
        session.close()
        return True
    except Exception:
        return False


def get_user_by_slug(slug: str):
    try:
        session = Session()
        user = session.query(User).filter_by(profileSlug=slug).first()
        session.close()
        return UserOut.from_orm(user)
    except Exception:
        return False


def get_user_by_name_password(username: str, password: str):
    session = Session()
    user = session.query(User).filter_by(userName=username, password=password).first()
    session.close()
    return UserOut.from_orm(user).profileSlug





def user_delete_by_slug(slug: str):
    session = Session()
    user = session.query(User).filter_by(profileSlug=slug).first()
    if user:
        session.delete(user)
        session.commit()
        session.close()
        print(f"User with id {slug} deleted successfully!")
        return True
    else:
        print(f"User with id {slug} not found.")
        session.close()
        return False







def user_update_name_email(slug: str, name=None, email=None) -> bool:
    session = Session()
    user = session.query(User).filter_by(profileSlug=slug).first()
    if user:
        if name:
            user.name = name
        if email:
            user.email = email
        session.commit()
        session.close()
        print(f"User with id {slug} updated successfully!")
        return True

    else:
        print(f"User with id {slug} not found.")
        session.close()
        return False
    










###



from pydantic import BaseModel

# Define a Pydantic data model for a User
class UserOut(BaseModel):
    id: int
    userName: str
    email: str
    profileUrl: str
    profileSlug: str
    password: str
    class Config:
        orm_mode = True

