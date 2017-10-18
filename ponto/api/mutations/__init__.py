import graphene
from ponto.api.mutations import user


class Mutation(graphene.ObjectType):
	sumation = graphene.NonNull(graphene.Int, a=graphene.NonNull(graphene.Int), b=graphene.NonNull(graphene.Int))
	create_account = user.CreateAccount.Field()

	def resolve_sumation(self, args, context, info):
		return args.get('a') + args.get('b')
