from django.urls import path

from rest.v1.auth import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'auth'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
