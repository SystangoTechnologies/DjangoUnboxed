from django.db import transaction
from rest_framework import serializers

from boilerplate_app.models import User, Projects


class ProjectsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('project_name', 'user')

    def create(self, validated_data):
        user = User.objects.get(pk=validated_data.pop('user'))
        return Projects.objects.create(**validated_data, user=user)


class ProjectsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'project_name', 'user')
