from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerfilUsuarioViewSet
from .views import PublicacionViewSet
from .views import ComentarioViewSet
from .views import LikeViewSet

router = DefaultRouter()
router.register(r'perfiles', PerfilUsuarioViewSet, basename='perfil')
router.register(r'publicaciones', PublicacionViewSet, basename='publicacion')
router.register(r'comentarios', ComentarioViewSet, basename='comentario')
router.register(r'likes', LikeViewSet, basename='like')

urlpatterns = [
    path('', include(router.urls)),
]