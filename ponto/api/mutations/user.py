import graphene
from ponto.api import types, exceptions
from ponto.db import functions


class CreateAccount(graphene.Mutation):
	class Input:
		email = graphene.NonNull(graphene.String)
		password = graphene.NonNull(graphene.String)

	session = graphene.Field(types.Session)

	@staticmethod
	def mutate(root, args, context, info):
		if functions.email_in_use(args.get('email')):
			raise exceptions.GenericError('Email in Use')
		user_id = functions.create_account(args.get('email'), args.get('password'))
		session = functions.create_session(user_id)
		return CreateAccount(session=session)

