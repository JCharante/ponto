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
