#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Python imports.
import logging

# Django imports.
from django.conf.urls import url

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


urlpatterns = [
    url(r'^test/$', TestAppAPIView.as_view(), name='boilerplate_app'),
    url(r'^register/$', RegistrationAPIView.as_view(), name='register-api'),
    url(r'^login/$', LoginView.as_view(), name='login-api'),
    url(r'^logout/$', LogoutView.as_view(), name='logout-api'),
    url(r'^list/users/$', UserAPIView.as_view(), name='user-api'),
    url(r'^project/$', ProjectAPIView.as_view(), name='project-api'),
    url(r'^docs/$', schema_view, name="schema_view"),
]