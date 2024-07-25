from django.urls import path
from . import views

# Definindo a url para acessar o index
urlpatterns = [
    path('avatarapp/', views.index, name='index'),
]