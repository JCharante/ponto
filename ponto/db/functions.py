from uuid import uuid4
import datetime
from ponto import db
from ponto.api import exceptions, types
from ponto.vendor import pavlok
import bcrypt
from typing import Tuple, List


def create_account(
	email: str,
	password: str,
	user_id=None
) -> str:
	"""

	:param email: Must be unique per account
	:param password:
	:param user_id: (Optional) If not supplied it will be generated. Should be uuid4
	:return:
	"""
	user_id = str(uuid4()) if user_id is None else user_id

	hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

	db_session = db.DBSession()

	db_session.add(db.UserV1(
		user_id=user_id,
		email=email,
		hashed_password=hashed_password
	))
	db_session.commit()
	db_session.close()
	return user_id


def create_session(
	user_id: str,
) -> types.Session:
	session_id = str(uuid4())
	valid_until = datetime.datetime.utcnow() + datetime.timedelta(days=365)  # TODO: Use a env. var
	db_session = db.DBSession()
	db_session.add(db.SessionV1(
		session_id=session_id,
		user_id=user_id,
		valid_until=valid_until
	))
	db_session.commit()
	db_session.close()
	return types.Session(
		session_id=session_id,
		valid_until=valid_until,
		user_id=user_id
	)


def email_in_use(
	email: str,
) -> bool:
	db_session = db.DBSession()
	row = db_session.query(db.UserV1).filter(db.UserV1.email == email).first()
	db_session.close()
	return row is not None


def verify_password(
	email: str,
	password: str,
) -> bool:
	db_session = db.DBSession()
	row = db_session.query(db.UserV1).filter(db.UserV1.email == email).first()  # type: db.UserV1
	db_session.close()
	if row is None:
		return False
	return bcrypt.checkpw(password.encode('utf-8'), row.hashed_password.encode('utf-8'))


def create_pavlok_key(
	user_id: str,
	client_id: str,
	client_secret: str,
	callback_url: str,
	code: str,
) -> types.PavlokKey:
	"""
	Requests and Creates a key for Pavlok from the auth code.
	:param user_id: the id of the user
	:param client_id: the client id from the registered pavlok application
	:param client_secret: the secret from the registered pavlok application
	:param callback_url: the callback_url used to create the refresh token
	:param code: the code obtained from authorizing the pavlok application
	:return:
	"""
	access_token, refresh_token, expires_in = pavlok.get_access_token_and_refresh_token(
		client_id,
		client_secret,
		callback_url,
		code,
	)
	key_id = str(uuid4())
	db_session = db.DBSession()
	db_session.add(db.PavlokKeyV1(
		key_id=key_id,
		client_id=client_id,
		client_secret=client_secret,
		callback_url=callback_url,
		access_token=access_token,
		refresh_token=refresh_token,
		user_id=user_id,
		expires_on=datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in),
	))
	db_session.commit()
	db_session.close()
	return types.PavlokKey(
		key_id=key_id,
		user_id=user_id
	)
