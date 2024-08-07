import os
import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ARRAY, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.getenv('DATABASE_URL'), echo=False)
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    oauth_id = Column(String, unique=True)
    telegram_id = Column(Integer, unique=True)

    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)

    score = Column(Integer, default=0)
    banned = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"ID: {self.telegram_id}"

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'score': self.score
        }


class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    value = Column(Integer, unique=True)
    name_question = Column(String)
    description = Column(String)
    is_solved = Column(ARRAY(Integer))

    def __repr__(self):
        return f"{self.value} | USERNAME: {self.name_question}"

    def to_dict(self):
        return {
            'name_question': self.name_question,
            'description': self.description
        }


class Solved(Base):
    __tablename__ = 'solved'
    id = Column(Integer, primary_key=True)
    customer = Column(Integer, unique=True)
    executors = Column(ARRAY(Integer))
