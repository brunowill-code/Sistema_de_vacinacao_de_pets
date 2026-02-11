from rest_framework.routers import DefaultRouter
from .views import (
    VacinaViewSet,
    VacinacaoViewSet
)

router = DefaultRouter()
router.register("vacina", VacinaViewSet, basename="vacinas")
router.register("vacinacao", VacinacaoViewSet, basename="vacinacao")


urlpatterns = router.urls