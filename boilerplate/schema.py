import graphene

import boilerplate_app.graphql.schema
import boilerplate_app.graphql.mutations


class Query(boilerplate_app.graphql.schema.Query, graphene.ObjectType):
    pass


class Mutation(boilerplate_app.graphql.mutations.Mutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
