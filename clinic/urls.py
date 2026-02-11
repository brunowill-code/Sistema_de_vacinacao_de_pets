from rest_framework.routers import DefaultRouter
from .views import (
    ClinicaViewSet,
    TutorViewSet,
    ProfissionalViewSet
)

router = DefaultRouter()
router.register("clinica", ClinicaViewSet, basename="clinica")
router.register("tutor", TutorViewSet, basename="tutor")
router.register("profissional", ProfissionalViewSet, basename="profissional")

urlpatterns = router.urls