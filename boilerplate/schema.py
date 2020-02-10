import graphene

import boilerplate_app.schema


class Query(boilerplate_app.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
