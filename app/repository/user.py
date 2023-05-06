from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a connection to the Postgres database
engine = create_engine('postgresql://username:password@host:port/database')

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Define a User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    userName = Column(String)
    email = Column(String, unique=True)
    profileUrl = 
    profileSlug
    password


    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userName', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('profileUrl', sa.String(), nullable=True),
    sa.Column('profileSlug', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')

# Create the users table in the database
Base.metadata.create_all(engine)

# Create a new User record
user = User(name='John Doe', email='john.doe@example.com')

# Add the User record to the database
session = Session()
session.add(user)
session.commit()

# Close the session
session.close()
