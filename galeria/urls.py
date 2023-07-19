from . import views
from django.urls import path

urlpatterns = [
    path ('', views.galeria, name='index'),
    path ('imagem/<int:foto_id>', views.imagem, name='imagem'),
    path ('buscar', views.buscar, name='buscar'),
]
