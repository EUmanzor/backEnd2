from django.db import models
from django.conf import settings

str_habilitado = "Habilitado"
str_fecha_creacion = "Fecha Creación"
str_fecha_actualizacion = "Fecha Actualización"

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    biografia = models.CharField(max_length=300, blank=True, null=True)
    habilitado = models.BooleanField(str_habilitado, default=True)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)
    
    class Meta:
        db_table_comment = "extension del perfil de un usuario"
        
    def __str__(self):
        return f"Perfil de {self.usuario.username}"

class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='publicaciones')
    contenido = models.CharField(max_length=500)
    habilitado = models.BooleanField(str_habilitado, default=True)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)
    
    class Meta:
        db_table_comment = "publicaciones hechas"
        
    def __str__(self):
        return f'Publicacion de {self.autor.username} ({self.created_at:%Y-%m-%d})'

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios_realizados')
    contenido = models.CharField(max_length=300)
    habilitado = models.BooleanField(str_habilitado, default=True)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)
    
    class Meta:
        db_table_comment = "comentarios hechos en publicaciones"
        
    def __str__(self):
        return f'comentario de {self.autor.username} en {self.publicacion.id}'

class Like(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes_realizados')
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='likes')
    habilitado = models.BooleanField(str_habilitado, default=True)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)
    
    class Meta:
        unique_together = ("usuario", "publicacion")
        db_table_comment = "los me gusta de un post"
        
    def __str__(self):
        return f'{self.usuario.username} dio like a {self.publicacion.id}'