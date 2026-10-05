from django.shortcuts import render

# Create your views here.
def bienvenida(request):
    return render(request, 'bienvenida.html')

from rest_framework import viewsets, permissions
from .models import PerfilUsuario
from .models import Publicacion
from .models import Comentario
from .models import Like
from .serializers import PerfilUsuarioSerializer
from .serializers import PublicacionSerializer
from .serializers import ComentarioSerializer
from .serializers import LikeSerializer


class ComprobarPropietario(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Comprueba si el objeto tiene 'autor' o 'usuario'
        owner = getattr(obj, 'autor', getattr(obj, 'usuario', None))
        return owner == request.user

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all().select_related('usuario')
    serializer_class = PerfilUsuarioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ComprobarPropietario]
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all().select_related('autor').prefetch_related('comentarios__autor', 'likes')
    serializer_class = PublicacionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ComprobarPropietario]
    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all().select_related('autor', 'publicacion')
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ComprobarPropietario]
    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all().select_related('usuario', 'publicacion')
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated, ComprobarPropietario]
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)