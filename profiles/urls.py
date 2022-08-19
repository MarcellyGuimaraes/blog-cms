from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:pk>', views.perfil, name='perfil'),
    path('conta', views.conta, name='conta'),
    path('atualizarperfil', views.atualizarperfil, name='atualizarperfil'),
    path('deletarperfil', views.deletarperfil, name='deletarperfil')
]