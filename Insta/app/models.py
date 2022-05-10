import profile
from pydoc import describe
from pyexpat import model
from statistics import mode
from django.contrib.auth.models import User
from django.db import models

class usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    nome = models.CharField("Nome", max_length=150)
    bio = models.TextField(max_length=150)
    email = models.EmailField("E-mail", max_length=150)
    arroba = models.CharField(max_length=10, primary_key=True)
    profile = models.ImageField("Foto de perfil", blank=True, null=True)

    def __str__(self):
        return self.arroba

class post(models.Model):
    arroba = models.ForeignKey(usuario, on_delete=models.CASCADE)
    descricao = models.TextField("Descrição", max_length=150)
    data = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField()

    def __str__(self):
        return self.arroba.arroba