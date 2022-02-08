from django.urls import path, include


app_name = "rest"

urlpatterns = [
    path('v1/', include("rest.v1.urls")),
]
