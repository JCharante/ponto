import graphene
from ponto.api.mutations import user, pavlok
from ponto.db import functions


class Mutation(graphene.ObjectType):
	sumation = graphene.NonNull(graphene.Int, a=graphene.NonNull(graphene.Int), b=graphene.NonNull(graphene.Int))
	create_account = user.CreateAccount.Field()
	create_session = user.CreateSession.Field()
	pavlok = graphene.Field(pavlok.MutatePavlok, session_id=graphene.NonNull(graphene.ID))

	def resolve_sumation(self, args, context, info):
		return args.get('a') + args.get('b')

	def resolve_pavlok(self, args, context, info):
		return pavlok.MutatePavlok(user_id=functions.get_user_id(args.get('session_id')))
