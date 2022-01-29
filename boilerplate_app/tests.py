from model_mommy import mommy
from django.test import TestCase

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
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@gmail.com",
            "password": "qwerty1234",
            "role": "role"
        }
        user_serializer = UserCreateSerializer(data=request_data)
        if user_serializer.is_valid():
            pass
        else:
            message = ''
            for error in user_serializer.errors.values():
                message += " "
                message += error[0]

        user = User(username=request_data.get('username'), first_name=request_data.get('first_name'),
                    last_name=request_data.get('last_name'), email=request_data.get('email'),
                    password=request_data.get('password'), role=request_data.get('role'))

        assert request_data.get('username') == user_serializer.data.get('username')
        assert request_data.get('first_name') == user_serializer.data.get('first_name')
        assert request_data.get('last_name') == user_serializer.data.get('last_name')
        assert request_data.get('email') == user_serializer.data.get('email')
        assert request_data.get('role') == user_serializer.data.get('role')
