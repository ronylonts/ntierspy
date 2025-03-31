from typing import List, Optional
from data.models import Project
from data.repositories import ProjectRepository
from ..dtos import ProjectDTO
from ..exceptions import (
    ProjectNotFoundException,
    InvalidProjectDataException,
    UnauthorizedAccessException
)

class ProjectService:
    """Service métier pour la gestion des projets"""
    
    def __init__(self, project_repository: ProjectRepository):
        self.repository = project_repository
    
    def get_all_projects(self) -> List[Project]:
        return self.repository.get_all_projects()
    
    def get_project_by_id(self, project_id: int) -> Project:
        try:
            return self.repository.get_project_by_id(project_id)
        except Project.DoesNotExist as e:
            raise ProjectNotFoundException(str(e))
    
    def create_project(self, project_dto: ProjectDTO, requesting_user_id: int) -> Project:
        if not project_dto.title or not project_dto.manager_id:
            raise InvalidProjectDataException("Le titre et le manager sont obligatoires")
        
        if project_dto.start_date > project_dto.end_date:
            raise InvalidProjectDataException("La date de début doit être avant la date de fin")
        
        project_data = {
            'title': project_dto.title,
            'description': project_dto.description,
            'start_date': project_dto.start_date,
            'end_date': project_dto.end_date,
            'status': project_dto.status,
            'budget': project_dto.budget,
            'manager_id': project_dto.manager_id,
            'team_members': project_dto.team_member_ids
        }
        
        return self.repository.create_project(project_data)
    
    def update_project(self, project_id: int, project_dto: ProjectDTO, requesting_user_id: int) -> Project:
        project = self.get_project_by_id(project_id)
        
        # Vérification des permissions
        if project.manager_id != requesting_user_id:
            raise UnauthorizedAccessException("Seul le manager du projet peut le modifier")
        
        update_data = {
            'title': project_dto.title or project.title,
            'description': project_dto.description or project.description,
            'start_date': project_dto.start_date or project.start_date,
            'end_date': project_dto.end_date or project.end_date,
            'status': project_dto.status or project.status,
            'budget': project_dto.budget or project.budget,
            'team_members': project_dto.team_member_ids or list(project.team_members.values_list('id', flat=True))
        }
        
        if update_data['start_date'] > update_data['end_date']:
            raise InvalidProjectDataException("La date de début doit être avant la date de fin")
        
        return self.repository.update_project(project_id, update_data)
    
    def delete_project(self, project_id: int, requesting_user_id: int) -> None:
        project = self.get_project_by_id(project_id)
        
        if project.manager_id != requesting_user_id:
            raise UnauthorizedAccessException("Seul le manager du projet peut le supprimer")
        
        self.repository.delete_project(project_id)
    
    def get_user_projects(self, user_id: int) -> List[Project]:
        return self.repository.get_user_projects(user_id)
    
    def calculate_project_progress(self, project_id: int) -> float:
        project = self.get_project_by_id(project_id)
        return project.progress