from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

    


urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),

    #Registro
    path('api/' , include("accounts.urls")),
    
    #Clinica
    path('api/', include("clinic.urls")),

    #Pets
    path('api/', include("pets.urls")),

    #Vacincao
    path('api/', include("vaccines.urls")),

    #JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
