from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

app_name = 'tasks'  # Namespace maintenu

urlpatterns = [
    # API Endpoints (DRF)
    path('api/', views.TaskListAPIView.as_view(), name='api-task-list'),
    path('api/<int:pk>/', views.TaskDetailAPIView.as_view(), name='api-task-detail'),
    
    # Template Endpoints (HTML)
    path('', views.task_list_view, name='task-list'),
    path('create/', views.task_create_view, name='task-create'),
    path('<int:task_id>/', views.task_detail_view, name='task-detail'),
    
    # JWT Endpoint
    path('api/token/refresh/', TokenRefreshView.as_view(), name='api-token-refresh'),
]