from django.contrib import admin
from .models import PerfilUsuario
from .models import Publicacion
from .models import Comentario
from .models import Like

# Register your models here.
admin.site.register(PerfilUsuario)
admin.site.register(Publicacion)
admin.site.register(Comentario)
admin.site.register(Like)
