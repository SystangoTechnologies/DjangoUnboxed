from django.urls import path

from rest.v1.boilerplate_app import views


app_name = 'boilerplate_app'

urlpatterns = [
    path('project/', views.ProjectAPIView.as_view(), name='project-api'),
]
