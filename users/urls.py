from django.urls import path
from . import views

app_name = 'users'  # Namespace pour les URLs

urlpatterns = [
    path('', views.user_list, name='user_list'),  # Page d'accueil users
    # Ajoutez d'autres URLs au besoin
]