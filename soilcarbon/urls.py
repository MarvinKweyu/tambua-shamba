from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

app_name = "soilcarbon"

router.register("", views.CarbonViewSet, basename="carbon")

urlpatterns = []

urlpatterns += router.urls
