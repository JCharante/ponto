import graphene
from ponto.api import types
from ponto.db import functions


class QueryPavlok(graphene.ObjectType):
	user_id = graphene.NonNull(graphene.ID)

	keys = graphene.NonNull(graphene.List(types.PavlokKey))

	def resolve_keys(self, args, context, info):
		return functions.get_pavlok_keys(str(self.user_id))
