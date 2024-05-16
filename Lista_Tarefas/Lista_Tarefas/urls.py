
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lista.api.views import ListaViewSet
from contas.api.views import RegisterAPI, LoginApi
from knox import views as knox_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


router = DefaultRouter()
router.register('api/Lista', ListaViewSet, basename='lista')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cadastrar/', RegisterAPI.as_view(), name='cadastrar'),
    path('api/login/', LoginApi.as_view(), name='login'),
   
   # open api 2
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', include(router.urls),)
]
