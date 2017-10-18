import graphene
from ponto.api import types
from ponto.db import functions


class PavlokAddKey(graphene.Mutation):
	class Input:
		client_id = graphene.NonNull(graphene.ID)
		client_secret = graphene.NonNull(graphene.ID)
		callback_url = graphene.NonNull(graphene.String)
		code = graphene.NonNull(graphene.ID)

	pavlok_key = graphene.Field(graphene.NonNull(types.PavlokKey))

	@staticmethod
	def mutate(root, args, context, info):
		pavlok_key = functions.create_pavlok_key(
			root.user_id,
			args.get('client_id'),
			args.get('client_secret'),
			args.get('callback_url'),
			args.get('code')
		)
		return PavlokAddKey(pavlok_key=pavlok_key)


class MutatePavlok(graphene.ObjectType):
	user_id = graphene.NonNull(graphene.ID)

	pavlok_add_key = PavlokAddKey.Field()
