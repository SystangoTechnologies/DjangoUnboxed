#!/usr/bin/env python

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Python imports.
import logging
import datetime
import calendar

# Django imports.
from django.db import transaction

# Rest Framework imports.
from rest_framework import serializers

# Third Party Library imports

# local imports.
from boilerplate_app.models import User, Projects


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate(self, data, *args, **kwargs):
       return super(UserCreateSerializer, self).validate(data, *args, **kwargs)

    @transaction.atomic()
    def create(self, validated_data):
        # Register new users
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    

    class Meta:
        model = User
        fields = ('email', 'id', 'password', 'username', 'first_name', 'last_name', 'role')
        extra_kwargs = {'password':{'write_only':True}}

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'role')


class ProjectsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = ('project_name','user')

    def create(self, validated_data):
        user = User.objects.get(pk=validated_data.pop('user'))
        return Projects.objects.create(**validated_data,user=user)


class ProjectsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = ('id', 'project_name', 'user')