from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, create_engine, Text, DATETIME, JSON
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()


class UserV1(Base):
	__tablename__ = 'UserV1'
	user_id = Column(String(36), primary_key=True)
	username = Column(Text(collation='utf8_general_ci'))
	hashed_password = Column(Text(collation='utf8_general_ci'))


class SessionV1(Base):
	__tablename__ = 'SessionV1'
	session_id = Column(String(36), primary_key=True)
	valid_until = Column(DATETIME)


class PavlokKeyV1(Base):
	__tablename__ = 'PavlokKeyV1'
	key_id = Column(String(36), primary_key=True)
	client_id = Column(String(64))
	secret = Column(String(64))
	callback_url = Column(Text())
	access_token = Column(String(64))
	refresh_token = Column(String(64))
