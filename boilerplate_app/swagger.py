from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


# Swagger test API
schema_view = get_schema_view(
        openapi.Info(
        title="Rest Swagger", default_version="v1", description="Test description"
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
)
