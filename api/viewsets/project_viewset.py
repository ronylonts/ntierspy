from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from data.repositories import ProjectRepository
from business.services import ProjectService
from .serializers import ProjectSerializer
from ..permissions import IsProjectManagerOrReadOnly

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsProjectManagerOrReadOnly]
    
    def get_queryset(self):
        project_repo = ProjectRepository()
        project_service = ProjectService(project_repo)
        return project_service.get_user_projects(self.request.user.id)
    
    def perform_create(self, serializer):
        project_repo = ProjectRepository()
        project_service = ProjectService(project_repo)
        project_dto = serializer.validated_data
        project = project_service.create_project(project_dto, self.request.user.id)
        serializer.instance = project
    
    def perform_update(self, serializer):
        project_repo = ProjectRepository()
        project_service = ProjectService(project_repo)
        project_dto = serializer.validated_data
        project_dto.id = self.kwargs['pk']
        project = project_service.update_project(
            project_dto.id, 
            project_dto, 
            self.request.user.id
        )
        serializer.instance = project
    
    def perform_destroy(self, instance):
        project_repo = ProjectRepository()
        project_service = ProjectService(project_repo)
        project_service.delete_project(instance.id, self.request.user.id)
    
    @action(detail=True, methods=['get'])
    def progress(self, request, pk=None):
        project_repo = ProjectRepository()
        project_service = ProjectService(project_repo)
        try:
            progress = project_service.calculate_project_progress(pk)
            return Response({'progress': progress}, status=status.HTTP_200_OK)
        except ProjectService.ProjectNotFoundException as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['get'])
    def my_projects(self, request):
        project_repo = ProjectRepository()
        project_service = ProjectService(project_repo)
        projects = project_service.get_user_projects(request.user.id)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)