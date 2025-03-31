from django.core.exceptions import ObjectDoesNotExist
from ..models import Project

class ProjectRepository:
    """Repository pour la gestion des opérations CRUD sur les projets"""
    
    @staticmethod
    def get_all_projects():
        return Project.objects.all().select_related('manager').prefetch_related('team_members', 'tasks')
    
    @staticmethod
    def get_project_by_id(project_id):
        try:
            return Project.objects.get(pk=project_id)
        except ObjectDoesNotExist:
            raise Project.DoesNotExist(f"Projet avec l'ID {project_id} n'existe pas")
    
    @staticmethod
    def create_project(project_data):
        team_members = project_data.pop('team_members', [])
        project = Project.objects.create(**project_data)
        project.team_members.set(team_members)
        return project
    
    @staticmethod
    def update_project(project_id, project_data):
        project = ProjectRepository.get_project_by_id(project_id)
        team_members = project_data.pop('team_members', None)
        
        for attr, value in project_data.items():
            setattr(project, attr, value)
        
        if team_members is not None:
            project.team_members.set(team_members)
        
        project.save()
        return project
    
    @staticmethod
    def delete_project(project_id):
        project = ProjectRepository.get_project_by_id(project_id)
        project.delete()
    
    @staticmethod
    def get_user_projects(user_id):
        return Project.objects.filter(
            models.Q(manager_id=user_id) | 
            models.Q(team_members__id=user_id)
        ).distinct()
    
    @staticmethod
    def get_projects_by_status(status):
        return Project.objects.filter(status=status)