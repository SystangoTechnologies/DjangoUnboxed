import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from ..models import User, Projects


class UserNode(DjangoObjectType):

    class Meta:
        model = User
        filter_fields = ["id", "first_name", "last_name", "role", "email"]
        interfaces = (relay.Node, )


class ProjectsNode(DjangoObjectType):

    class Meta:
        model = Projects
        filter_fields = {
            'project_name': ['exact', 'icontains', 'istartswith'],
            'user__email': ['exact']
        }
        interfaces = (relay.Node, )


class Query(ObjectType):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    project = relay.Node.Field(ProjectsNode)
    all_projects = DjangoFilterConnectionField(ProjectsNode)


schema = graphene.Schema(Query)
