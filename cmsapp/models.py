from django.db import models
import uuid
from ckeditor.fields import RichTextField
from profiles.models import UserProfile

# Create your models here.


class Post(models.Model):
    escritor = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    titulo = models.CharField(max_length=500)
    imagem = models.ImageField(upload_to='img/')
    texto = RichTextField()
    post_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    categoria_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    slug = models.SlugField()

    def __str__(self):
        return self.titulo