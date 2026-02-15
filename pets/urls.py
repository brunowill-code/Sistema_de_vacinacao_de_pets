from rest_framework.routers import DefaultRouter
from .views.pets_view import (
    PetsViewSet
)

router = DefaultRouter()
router.register("pets", PetsViewSet, basename="pets")


urlpatterns = router.urls