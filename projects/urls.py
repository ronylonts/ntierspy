from django.urls import path
from . import views
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView
)

app_name = 'projects'

urlpatterns = [
    # Version avec vues basées sur les classes
    path('', ProjectListView.as_view(), name='list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='detail'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete'),
    
    # OU version avec vues fonctionnelles
    # path('', views.project_list, name='list'),
]