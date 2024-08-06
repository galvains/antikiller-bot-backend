import os
import datetime

from sqlalchemy import create_engine, Integer, String, Boolean, Column, UniqueConstraint, ForeignKey, DateTime, Text, \
    JSON, ARRAY
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine(os.getenv('DATABASE_URL'), echo=True)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    # for api
    oauth_id = Column(Integer, unique=True)
    telegram_id = Column(Integer, unique=True)

    # for qr-code generated
    secret_code = Column(Integer)
    banned = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    quests = Column(ARRAY(Integer))

    users = relationship('Profiles', back_populates='users')

    def __repr__(self):
        return f"ID: {self.telegram_id}"


class Profiles(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(ForeignKey('users.telegram_id', ondelete="CASCADE"), nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    photo = Column(String)

    questions = Column(Integer)

    oauth = relationship('Users', back_populates='profiles')

    def __repr__(self):
        return f"{self.telegram_id} | USERNAME: {self.username}"


class Quests(Base):
    __tablename__ = 'quests'
    id = Column(Integer, primary_key=True)
    value = Column(Integer, unique=True)
    name_question = Column(String)
    description = Column(String)

    def __repr__(self):
        return f"{self.value} | USERNAME: {self.name_question}"
