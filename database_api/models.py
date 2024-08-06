import os
import datetime

from sqlalchemy import create_engine, Integer, String, Boolean, Column, UniqueConstraint, ForeignKey, DateTime, Text, \
    JSON
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine(os.getenv('DATABASE_URL'), echo=True)


class Users(Base):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint("id", "oauth_id"), {})

    id = Column(Integer, primary_key=True)
    oauth_id = Column(Integer, unique=True)

    username = Column(String(128), unique=True)
    points = Column(Integer)

    banned = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.id!r}"
