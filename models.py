from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    userName = Column(String)
    email = Column(String)
    profileUrl = Column(String)
    profileSlug = Column(String)
    password = Column(String)
