import graphene
from ponto.api.queries import Query
from ponto.api.mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
