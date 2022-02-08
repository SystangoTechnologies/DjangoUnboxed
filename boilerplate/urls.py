from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import urls

from graphene_django.views import GraphQLView

from boilerplate_app.swagger import schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(urls)),
    path('api/', include("rest.urls", namespace='rest')),
    path('api/documentation/', schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
