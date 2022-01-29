from django.urls import path, include


urlpatterns = [
    path('authorization/', include("rest.v1.authorization.urls")),
    path('boilerplate-app/', include("rest.v1.boilerplate_app.urls")),
]
