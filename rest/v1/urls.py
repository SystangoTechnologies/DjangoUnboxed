from django.urls import path, include


urlpatterns = [
    path('boilerplate-app/', include("rest.v1.boilerplate_app.urls")),
]
