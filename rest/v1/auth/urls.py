from django.urls import path

from rest.v1.auth import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


app_name = 'auth'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('token/', obtain_jwt_token, name='token_obtain_pair'),
    path('token/refresh/', refresh_jwt_token, name='refresh_jwt_token'),
]
