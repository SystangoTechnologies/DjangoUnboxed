from django.urls import path, include


urlpatterns = [
    path('auth/', include("rest.v1.auth.urls")),
    path('boilerplate-app/', include("rest.v1.boilerplate_app.urls")),
]
