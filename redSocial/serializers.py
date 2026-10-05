from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import PerfilUsuario
from .models import Publicacion
from .models import Comentario
from .models import Like

UsuarioSimple = get_user_model()
class UsuarioSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioSimple
        fields = ['id', 'username', 'email']

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    usuario = UsuarioSimpleSerializer(read_only=True)
    class Meta:
        model = PerfilUsuario
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    autor = UsuarioSimpleSerializer(read_only=True)
    class Meta:
        model = Comentario
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    usuario = UsuarioSimpleSerializer(read_only=True)
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class PublicacionSerializer(serializers.ModelSerializer):
    autor = UsuarioSimpleSerializer(read_only=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)
    total_likes = serializers.IntegerField(source='likes.count', read_only=True)
    class Meta:
        model = Publicacion
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']