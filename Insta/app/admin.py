from django.contrib import admin
from .models import usuario, post

@admin.register(usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass

@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    pass