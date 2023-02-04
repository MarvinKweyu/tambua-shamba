from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

app_name = "soilcarbon"

router.register("farms", views.FarmViewSet, basename="farms")
router.register("sources", views.SourceFileViewSet, basename="source_file")

urlpatterns = []

urlpatterns += router.urls
