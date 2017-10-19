from ponto.api import schema
from uuid import uuid4


generated_email = f"test.ponto.{str(uuid4())[:8]}@jcharante.com"
generated_password = str(uuid4())[:8]


def test_create_account():
	query = """
	mutation ($email: String!, $password: String!) {
		createAccount(email: $email, password: $password) {
			session {
				sessionId
				validUntil
				userId
			}
		}
	}
	"""
	variables = {
		'email': generated_email,
		'password': generated_password
	}
	result = schema.execute(query, variable_values=variables)
	assert len(result.data['createAccount']['session']['sessionId']) == 36


def test_account_login():
	query = """
		mutation ($email: String!, $password: String!) {
			createSession(email: $email, password: $password) {
				session {
					sessionId
					validUntil
					userId
				}
			}
		}
		"""
	variables = {
		'email': generated_email,
		'password': generated_password
	}
	result = schema.execute(query, variable_values=variables)
	assert len(result.data['createSession']['session']['sessionId']) == 36


if __name__ == "__main__":
	test_create_account()
	test_account_login()
