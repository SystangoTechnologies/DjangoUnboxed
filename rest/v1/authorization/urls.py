from django.urls import path

from rest.v1.authorization import views


app_name = 'authorization'

urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view(), name='register-api'),
    path('login/', views.LoginView.as_view(), name='login-api'),
    path('logout/', views.LogoutView.as_view(), name='logout-api'),
    path('list/users/', views.UserAPIView.as_view(), name='user-api'),
]
