from rest_framework.routers import DefaultRouter
from .views.clinica_views import ClinicaViewSet
from .views.tutor_views import TutorViewSet
from .views.profissional_views import ProfissionalViewSet

router = DefaultRouter()
router.register("clinica", ClinicaViewSet, basename="clinica")
router.register("tutor", TutorViewSet, basename="tutor")
router.register("profissional", ProfissionalViewSet, basename="profissional")

urlpatterns = router.urls