import graphene
from ponto.api.queries import pavlok
from ponto.db import functions


class Query(graphene.ObjectType):
	motd = graphene.NonNull(graphene.String)
	pavlok = graphene.Field(pavlok.QueryPavlok, session_id=graphene.NonNull(graphene.ID))

	def resolve_motd(self, args, context, info):
		return 'Hello'

	def resolve_pavlok(self, args, context, info):
		return pavlok.QueryPavlok(user_id=functions.get_user_id(args.get('session_id')))
