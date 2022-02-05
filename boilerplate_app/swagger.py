from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view


# Swagger API
schema_view = get_schema_view(
    openapi.Info(
        title="DjangoUnboxed Rest API",
        default_version="v1"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url=""
)
