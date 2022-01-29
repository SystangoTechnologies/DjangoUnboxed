from rest_framework import status
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from boilerplate_app.utils import generate_jwt_token
from rest.v1.authorization.serializers import UserCreateSerializer, UserListSerializer

User = get_user_model()


class RegistrationAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

    __doc__ = "Registration API for user"

    def post(self, request, *args, **kwargs):
        try:
            user_serializer = self.serializer_class(data=request.data)
            if user_serializer.is_valid():
                user = user_serializer.save()
                data = generate_jwt_token(user, user_serializer.data)
                return Response(data, status=status.HTTP_200_OK)
            else:
                message = ''
                for error in user_serializer.errors.values():
                    message += " "
                    message += error[0]
                return Response({'status': False,
                                 'message': message},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': False,
                             'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class LoginView(JSONWebTokenAPIView):
    serializer_class = JSONWebTokenSerializer

    __doc__ = "Log In API for user which returns token"

    @staticmethod
    def post(request):
        try:
            serializer = JSONWebTokenSerializer(data=request.data)
            if serializer.is_valid():
                serialized_data = serializer.validate(request.data)
                user = User.objects.get(email=request.data.get('email'))
                return Response({
                    'status': True,
                    'token': serialized_data['token'],
                }, status=status.HTTP_200_OK)
            else:
                message = ''
                for error in serializer.errors.values():
                    message += " "
                    message += error[0]
                return Response({'status': False,
                                 'message': message},
                                status=status.HTTP_400_BAD_REQUEST)
        except (AttributeError, ObjectDoesNotExist):
            return Response({'status': False,
                             'message': "User does not exist"},
                            status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        """
        Logout API for user
        """
        try:
            user = request.user
            logout(request)
            return Response({'status': True,
                             'message': "logout successfully"},
                            status=status.HTTP_200_OK)
        except (AttributeError, ObjectDoesNotExist):
            return Response({'status': False},
                            status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(GenericAPIView):
    serializer_class = UserListSerializer

    def get(self, request, format=None):
        """
        List all the users.
        """
        try:
            users = User.objects.all()
            user_serializer = UserListSerializer(users, many=True)

            users = user_serializer.data
            return Response({'status': True,
                             'Response': users},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
