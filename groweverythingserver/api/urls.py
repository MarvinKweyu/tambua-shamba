from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.documentation import include_docs_urls

API_TITLE = "The GrowEverything SoilCarbon API"
API_DESCRIPTION = (
    "A project to collect and preview soil organic carbon performance in farms across Kenya"
)

schema_view = get_schema_view(
    openapi.Info(
        title="The GrowEverything SoilCarbon API",
        default_version="v1",
        description="Soil carbon content across farms in Kenya",
        terms_of_service="",
        contact=openapi.Contact(email="mkweyu1@gmail.com "),
    ),
    public=True,
)

urlpatterns = [
    path("soilcarbon/", include("soilcarbon.urls")),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),
    path("docs/", include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    # path('new/schema/swagger-ui/',
    #      SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(
        "schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
]
