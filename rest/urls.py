from django.urls import path, include

from boilerplate_app.swagger import schema_view

urlpatterns = [
    path('v1/', include("rest.v1.urls")),
    path('documentation/', schema_view.with_ui("swagger", cache_timeout=0), name="schema_view"),
]
