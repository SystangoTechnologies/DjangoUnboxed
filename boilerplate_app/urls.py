#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Python imports.
import logging

# Django imports.
from django.urls import path,include

# Rest Framework imports.

# Third Party Library imports

# local imports.
from boilerplate_app.views import (
                          TestAppAPIView, 
                          UserAPIView, 
                          ProjectAPIView, 
                          RegistrationAPIView,
                          LoginView,
                          LogoutView
                          )
from boilerplate_app.swagger import schema_view




app_name = 'boilerplate_app'

urlpatterns = [
    path('test/', TestAppAPIView.as_view(), name='boilerplate_app'),
    path('register/', RegistrationAPIView.as_view(), name='register-api'),
    path('login/', LoginView.as_view(), name='login-api'),
    path('logout/', LogoutView.as_view(), name='logout-api'),
    path('list/users/', UserAPIView.as_view(), name='user-api'),
    path('project/', ProjectAPIView.as_view(), name='project-api'),
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0), name="schema_view"),
]
