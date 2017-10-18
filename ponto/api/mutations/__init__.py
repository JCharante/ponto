import graphene


class Mutation(graphene.ObjectType):
	sumation = graphene.NonNull(graphene.Int, a=graphene.NonNull(graphene.Int), b=graphene.NonNull(graphene.Int))

	def resolve_sumation(self, args, context, info):
		return args.get('a') + args.get('b')
