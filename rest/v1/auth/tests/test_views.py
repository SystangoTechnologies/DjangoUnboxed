from typing import Tuple

import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from authorization.tests import factories as user_factories

User = get_user_model()


@pytest.fixture()
def rest_client() -> APIClient:
    return APIClient()


@pytest.fixture()
def rest_client_with_user(rest_client) -> Tuple[User, APIClient]:
    user = user_factories.UserFactory()
    rest_client.force_authenticate(user=user)
    return user, rest_client


@pytest.mark.django_db
def test_auth__signup__success(rest_client):
    new_user_email = 'user1@gmail.com'
    response = rest_client.post(
        '/api/v1/auth/signup/',
        {
            'password': 'some password',
            'email': new_user_email,
        },
        format='json',
    )

    assert response.status_code == 201

    user = User.objects.all().first()
    assert user is not None
    assert user.email == new_user_email


@pytest.mark.django_db
def test_auth__signup__fail__invalid_email(rest_client):
    response = rest_client.post(
        '/api/v1/auth/signup/',
        {
            'password': 'some password',
            'email': 'user1',
        },
        format='json',
    )

    assert response.status_code == 400
    assert not response.data['status']
    assert response.data['errors']['email'][0].title() == 'Enter A Valid Email Address.'


@pytest.mark.django_db
def test_auth__signup__fail__no_data_provided(rest_client):
    response = rest_client.post('/api/v1/auth/signup/')

    assert response.status_code == 400
    assert not response.data['status']
    assert response.data['errors']['email'][0].title() == \
           response.data['errors']['password'][0].title() == 'This Field Is Required.'


@pytest.mark.django_db
def test_auth__token__success(rest_client):
    response = rest_client.post(
        '/api/v1/auth/signup/',
        {
            'password': '123456789',
            'email': 'test@gmail.com',
        },
        format='json',
    )

    assert response.status_code == 201
    user = User.objects.all().first()

    response = rest_client.post(
        '/api/v1/auth/token/',
        {
            'password': '123456789',
            'email': user.email
        },
        format='json',
    )

    assert response.status_code == 200
    token = response.data['token']

    response = rest_client.post(
        '/api/v1/auth/token/refresh/',
        {
            'token': token
        },
        format='json',
    )

    assert response.status_code == 200
    assert 'refresh' in response['data']
