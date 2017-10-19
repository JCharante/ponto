import requests
from ponto.api import exceptions
from typing import Tuple

BASE_API_ENDPOINT = 'https://pavlok-mvp.herokuapp.com'


def get_access_token_and_refresh_token(
	client_id: str,
	client_secret: str,
	callback_url: str,
	code: str,
) -> Tuple[str, str, int]:
	"""

	:param client_id: the client id from the registered pavlok application
	:param client_secret: the client secret from the registered pavlok application
	:param callback_url: The callback url used to create the auth code
	:param code: The auth. code you get from authorizing the pavlok app
	:return: A tuple with three values [access_token: str, refresh_token: str, seconds until access token expires)
	"""
	payload = {
		"client_id": client_id,
		"client_secret": client_secret,
		"code": code,
		"grant_type": "authorization_code",
		"redirect_uri": callback_url,
	}

	r = requests.post(BASE_API_ENDPOINT + '/oauth/token', json=payload)
	response_data = r.json()
	if r.status_code != 200:
		raise exceptions.GenericError(response_data)
	return response_data.get('access_token'), response_data.get('refresh_token'), int(response_data.get('expires_in'))


def shock(
	access_token: str,
	value: int,
	reason: str=None,
) -> None:
	"""
	Sends a shock stimuli request to pavlok
	:param access_token: acess_token required to authenticate with pavlok's api
	:param value: Intensifier for the stimulus (1-255)
	:param reason: Reason to show in the Pavlok App under logs.
	:return:
	"""
	payload = {
		"access_token": access_token,
	}

	if reason is not None:
		payload['reason'] = reason

	r = requests.post(f"{BASE_API_ENDPOINT}/api/v1/stimuli/shock/{value}", json=payload)
	response_data = r.text
	if r.status_code != 200:
		raise exceptions.GenericError(response_data)


def vibration(
	access_token: str,
	value: int,
	reason: str=None
) -> None:
	"""
	Sends a vibration stimuli request to pavlok
	:param access_token:
	:param value: The value intensifier for the stimulus (1-255)
	:param reason:
	:return:
	"""

	payload = {
		"access_token": access_token,
	}

	if reason is not None:
		payload['reason'] = reason

	r = requests.post(f"{BASE_API_ENDPOINT}/api/v1/stimuli/vibration/{value}", json=payload)
	response_data = r.text
	if r.status_code != 200:
		raise exceptions.GenericError(response_data)


def led(
	access_token: str,
	value: int,
	reason: str=None
) -> None:
	"""
	Sends a LED stimulus to the associated pavlok
	:param access_token:
	:param value: The value intensifier for the stimulus (1-4)
	:param reason:
	:return:
	"""

	payload = {
		"access_token": access_token,
	}

	if reason is not None:
		payload['reason'] = reason

	r = requests.post(f"{BASE_API_ENDPOINT}/api/v1/stimuli/led/{value}", json=payload)
	response_data = r.text
	if r.status_code != 200:
		raise exceptions.GenericError(response_data)


def beep(
	access_token: str,
	value: int,
	reason: str=None
) -> None:
	"""
	Sends a beep stimulus to the associated pavlok
	:param access_token:
	:param value: The value intensifier for the stimulus (1-4)
	:param reason:
	:return:
	"""

	payload = {
		"access_token": access_token,
	}

	if reason is not None:
		payload['reason'] = reason

	r = requests.post(f"{BASE_API_ENDPOINT}/api/v1/stimuli/beep/{value}", json=payload)
	response_data = r.text
	if r.status_code != 200:
		raise exceptions.GenericError(response_data)
