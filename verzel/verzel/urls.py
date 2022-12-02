from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from vehicle.views import *
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Setting the routes to the [vehicle, modelo, fabricante] APIs
router = routers.DefaultRouter()
router.register(r'vehicle', VehicleViewSet)
router.register(r'modelo', ModeloViewSet)
router.register(r'fabricante', FabricanteViewSet)

# adding routes automatically
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)