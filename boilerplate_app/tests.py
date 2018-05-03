from model_mommy import mommy
from django.test import TestCase


from rest_framework_jwt.serializers import JSONWebTokenSerializer


from boilerplate_app.models import User
from boilerplate_app.serializers import UserListSerializer, UserCreateSerializer


class APITests(TestCase):

    def test_list_user(self):

        user = mommy.make(User)
        self.assertTrue(isinstance(user, User))

        user_serializer = UserListSerializer(user)

        assert user.id == user_serializer.data.get('id')
        assert user.first_name == user_serializer.data.get('first_name')
        assert user.last_name == user_serializer.data.get('last_name')
        assert user.email == user_serializer.data.get('email')
        assert user.role == user_serializer.data.get('role')

    def test_register(self):

        request_data = {
            "username": "username",
            "first_name" : "first_name",
            "last_name" : "last_name",
            "email" : "email@gmail.com",
            "password" : "qwerty1234",
            "role" : "role"
        }
        user_serializer = UserCreateSerializer(data=request_data)
        if user_serializer.is_valid():
            pass
        else:
            message = ''
            for error in user_serializer.errors.values():
                message += " "
                message += error[0]
            print(message)

        user = User(username=request_data.get('username'), first_name=request_data.get('first_name'), last_name=request_data.get('last_name'), email=request_data.get('email'), password=request_data.get('password'), role=request_data.get('role'))

        assert request_data.get('username') == user_serializer.data.get('username') 
        assert request_data.get('first_name') == user_serializer.data.get('first_name')
        assert request_data.get('last_name') == user_serializer.data.get('last_name')
        assert request_data.get('email') == user_serializer.data.get('email')
        assert request_data.get('role') == user_serializer.data.get('role')





# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# # Django imports
# from django.test import TestCase
# from django.urls import reverse

# # rest framework imports
# from rest_framework.test import APIClient
# from rest_framework import status

# # local imports
# from boilerplate_app.models import User


# # Create your tests here.


# class APITests(TestCase):

#     def setUp(self):
#         self.first_name = "ABC"
#         self.last_name = "XYZ"
#         self.email = "abc@gmail.com"
#         self.password = "abc12345678"
#         self.role = "Manager"
#         self.username = "Admin"
#         self.project_name = "XYZ"
#         self.URLS = {
#                     'register-api': reverse('boilerplate_app-api:register-api'),
#                     'login-api': reverse('boilerplate_app-api:login-api'),
#                     'user-api': reverse('boilerplate_app-api:user-api'),
#                     'project-api': reverse('boilerplate_app-api:project-api'),
#                      }

#     def register_user(self):
#         User.objects.create_user(email=self.email,
#                                  password=self.password,
#                                  first_name=self.first_name,
#                                  last_name=self.last_name,
#                                  role=self.role,
#                                  username=self.username
#                                  )

#     def login_user(self, client):
#         resp = client.post(self.URLS['login-api'],
#                            {'email': self.email, 'password': self.password})
#         return resp


#     def test_register(self):
#         client = APIClient()        
#         resp = client.post(self.URLS['register-api'],
#                            {'email': self.email, 'password': self.password,
#                             'confirm_password': self.password, 'first_name' : self.first_name,
#                             'last_name' : self.last_name, 'role' : self.role, 'username' : self.username
#                             }, format='json')
#         assert resp.status_code == status.HTTP_200_OK

#     def test_login(self):
#         client = APIClient()
#         User.objects.create_user(email=self.email,
#                                  password=self.password
#                                  )
#         resp = client.post(self.URLS['login-api'],
#                            {'email': self.email, 'password': self.password                            
#                             }, format='json'
#                            )
#         assert resp.status_code == status.HTTP_200_OK
#         assert resp.data['status']

#     def test_list_user(self):
#         client = APIClient()
#         self.register_user()
#         resp = self.login_user(client)
#         assert resp.status_code == status.HTTP_200_OK
#         assert resp.data['status']
#         token = resp.data['token']
#         client.credentials(HTTP_AUTHORIZATION='Token ' + token)
#         resp = client.get(self.URLS['user-api'])
#         assert resp.status_code == status.HTTP_200_OK

#     def test_list_project(self):
#         client = APIClient()
#         self.register_user()
#         resp = self.login_user(client)
#         assert resp.status_code == status.HTTP_200_OK
#         assert resp.data['status']
#         token = resp.data['token']
#         client.credentials(HTTP_AUTHORIZATION='Token ' + token)
#         resp = client.get(self.URLS['project-api'])
#         assert resp.status_code == status.HTTP_200_OK

#     def tearDown(self):
#         User.objects.filter(email=self.email).delete()
