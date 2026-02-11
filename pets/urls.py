from rest_framework.routers import DefaultRouter
from .views import (
    PetsViewSet
)

router = DefaultRouter()
router.register("pets", PetsViewSet, basename="pets")


urlpatterns = router.urls