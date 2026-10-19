from django.contrib import admin
from usuarios.models import Usuario, Adotante, Abrigo, Perfil

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Adotante)
admin.site.register(Abrigo)
admin.site.register(Perfil)
