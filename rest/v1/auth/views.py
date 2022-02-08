from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from rest.v1.auth.serializers import UserCreateSerializer

User = get_user_model()


class SignUpView(CreateAPIView):
    serializer_class = UserCreateSerializer

    __doc__ = "Registration API for user"

    def post(self, request, *args, **kwargs):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(
                {'status': False, 'errors': user_serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
