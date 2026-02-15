from rest_framework.routers import DefaultRouter
from vaccines.views.vacinacao_view import VacinacaoViewSet

from vaccines.views.vacina_view import VacinaViewSet

router = DefaultRouter()
router.register("vacina", VacinaViewSet, basename="vacinas")
router.register("vacinacao", VacinacaoViewSet, basename="vacinacao")

urlpatterns = router.urls