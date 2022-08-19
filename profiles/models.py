import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    nome_usuario = models.CharField(max_length=200)
    profissao = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='img', blank=True, null=True)
    sobre = models.TextField(max_length=500)
    id_perfil = models.UUIDField(default=uuid.uuid4,editable=False, unique=True, primary_key=True)

    def __str__(self):
        return self.nome_usuario