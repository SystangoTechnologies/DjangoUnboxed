from django.db import transaction
from rest_framework import serializers
from django.contrib.auth import get_user_model

from boilerplate_app.models import Projects

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate(self, data, *args, **kwargs):
        return super(UserCreateSerializer, self).validate(data, *args, **kwargs)

    @transaction.atomic()
    def create(self, validated_data):
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'first_name', 'last_name', 'role')
        extra_kwargs = {'password': {'write_only': True}}


class ProjectsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('project_name', 'user')

    def create(self, validated_data):
        user = User.objects.get(pk=validated_data.pop('user'))
        return Projects.objects.create(**validated_data, user=user)

