from django.urls import path, include


urlpatterns = [
    path('v1/', include("rest.v1.urls")),
]
