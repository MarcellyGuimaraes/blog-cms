from django.contrib import admin
from .models import Post, Categoria

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Categoria, CategoriaAdmin)