from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/boilerplate_apps/', include("boilerplate_app.urls", namespace="boilerplate_app-api")),
    path('api/', include("rest.urls")),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
