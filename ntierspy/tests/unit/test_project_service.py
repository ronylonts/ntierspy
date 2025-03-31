from django.test import TestCase
from django.contrib.auth import get_user_model
from data.models import Project
from data.repositories import ProjectRepository
from business.services import ProjectService
from business.dtos import ProjectDTO
from business.exceptions import (
    ProjectNotFoundException,
    InvalidProjectDataException,
    UnauthorizedAccessException
)
from datetime import date, timedelta

User = get_user_model()

class ProjectServiceTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='manager',
            email='manager@example.com',
            password='password',
            first_name='John',
            last_name='Doe'
        )
        self.team_member = User.objects.create_user(
            username='member',
            email='member@example.com',
            password='password',
            first_name='Jane',
            last_name='Smith'
        )
        self.project_data = {
            'title': 'Projet Test',
            'description': 'Description du projet test',
            'start_date': date.today(),
            'end_date': date.today() + timedelta(days=30),
            'status': 'DF',
            'budget': 10000.00,
            'manager_id': self.user.id,
            'team_member_ids': [self.team_member.id]
        }
        self.repository = ProjectRepository()
        self.service = ProjectService(self.repository)
    
    def test_create_project_success(self):
        project_dto = ProjectDTO(**self.project_data)
        project = self.service.create_project(project_dto, self.user.id)
        
        self.assertEqual(project.title, self.project_data['title'])
        self.assertEqual(project.manager_id, self.user.id)
        self.assertEqual(project.team_members.count(), 1)
    
    def test_create_project_missing_title(self):
        invalid_data = self.project_data.copy()
        invalid_data['title'] = ''
        project_dto = ProjectDTO(**invalid_data)
        
        with self.assertRaises(InvalidProjectDataException):
            self.service.create_project(project_dto, self.user.id)
    
    def test_get_project_by_id_success(self):
        project_dto = ProjectDTO(**self.project_data)
        project = self.service.create_project(project_dto, self.user.id)
        fetched_project = self.service.get_project_by_id(project.id)
        
        self.assertEqual(project.id, fetched_project.id)
    
    def test_get_project_by_id_not_found(self):
        with self.assertRaises(ProjectNotFoundException):
            self.service.get_project_by_id(999)
    
    def test_update_project_success(self):
        project_dto = ProjectDTO(**self.project_data)
        project = self.service.create_project(project_dto, self.user.id)
        
        update_data = {
            'id': project.id,
            'title': 'Projet Modifié',
            'description': 'Nouvelle description',
            'manager_id': self.user.id,
            'team_member_ids': [self.team_member.id]
        }
        updated_project = self.service.update_project(
            project.id,
            ProjectDTO(**update_data),
            self.user.id
        )
        
        self.assertEqual(updated_project.title, 'Projet Modifié')
    
    def test_update_project_unauthorized(self):
        project_dto = ProjectDTO(**self.project_data)
        project = self.service.create_project(project_dto, self.user.id)
        
        other_user = User.objects.create_user(
            username='other',
            email='other@example.com',
            password='password'
        )
        
        update_data = {
            'id': project.id,
            'title': 'Projet Modifié',
            'manager_id': self.user.id
        }
        
        with self.assertRaises(UnauthorizedAccessException):
            self.service.update_project(
                project.id,
                ProjectDTO(**update_data),
                other_user.id
            )
    
    def test_calculate_project_progress(self):
        project_dto = ProjectDTO(**self.project_data)
        project = self.service.create_project(project_dto, self.user.id)
        
        progress = self.service.calculate_project_progress(project.id)
        self.assertEqual(progress, 0.0)