import graphene
from graphene_django.rest_framework.mutation import SerializerMutation

from ..serializers import ProjectsCreateSerializer


class ProjectsMutation(SerializerMutation):

    class Meta:
        serializer_class = ProjectsCreateSerializer
        model_operations = ['create']


class Mutations(graphene.ObjectType):
    create_project = ProjectsMutation.Field()
