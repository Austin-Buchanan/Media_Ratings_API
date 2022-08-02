from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base

# create table models for video games, books, movies, etc.

class VideoGame(Base):
    __tablename__ = "video_games"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    developer = Column(String)
    # completed = Column(Boolean, server_default='True', nullable=False)
    rating = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class User(Base):
    __tablename__ = "users"
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))