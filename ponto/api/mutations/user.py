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


class CreateSession(graphene.Mutation):
	class Input:
		email = graphene.NonNull(graphene.String)
		password = graphene.NonNull(graphene.String)

	session = graphene.Field(graphene.NonNull(types.Session))

	@staticmethod
	def mutate(root, args, context, info):
		if functions.verify_password(args.get('email'), args.get('password')) is False:
			raise exceptions.GenericError('Invalid Email/Password Combination')
		user_id = functions.get_user_id(email=args.get('email'))
		session = functions.create_session(user_id)
		return CreateSession(session=session)
