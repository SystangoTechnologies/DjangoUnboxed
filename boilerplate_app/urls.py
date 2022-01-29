from django.urls import path

from boilerplate_app import views
from boilerplate_app.swagger import schema_view


app_name = 'boilerplate_app'

urlpatterns = [
    path('test/', views.TestAppAPIView.as_view(), name='boilerplate_app'),
    path('register/', views.RegistrationAPIView.as_view(), name='register-api'),
    path('login/', views.LoginView.as_view(), name='login-api'),
    path('logout/', views.LogoutView.as_view(), name='logout-api'),
    path('list/users/', views.UserAPIView.as_view(), name='user-api'),
    path('project/', views.ProjectAPIView.as_view(), name='project-api'),
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0), name="schema_view"),
]
