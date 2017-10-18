from graphene.types.datetime import DateTime
import graphene


class Session(graphene.ObjectType):
	session_id = graphene.NonNull(graphene.ID)
	valid_until = graphene.NonNull(graphene.types.datetime.DateTime)
	user_id = graphene.ID()


class PavlokKey(graphene.ObjectType):
	key_id = graphene.NonNull(graphene.ID)
	user_id = graphene.NonNull(graphene.ID)
