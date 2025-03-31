from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ProjectViewSet, TaskViewSet, UserViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]