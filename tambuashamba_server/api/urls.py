from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.documentation import include_docs_urls

API_TITLE = "The TambuaShamba Project API"
API_DESCRIPTION = (
    "A project to collect and preview soil organic carbon performance in farms across Kenya"
)

schema_view = get_schema_view(
    openapi.Info(
        title="The TambuaShamba Project API",
        default_version="v1",
        description="Soil carbon content across farms in Kenya",
        terms_of_service="",
        contact=openapi.Contact(email="hello@marvinkweyu.net "),
    ),
    public=True,
)

urlpatterns = [
    path("soilcarbon/", include("soilcarbon.urls")),
    path("docs/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
]
