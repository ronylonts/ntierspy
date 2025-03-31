from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from data.models import Project
from rest_framework import status
import json

User = get_user_model()

class PresentationLayerTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        self.project = Project.objects.create(
            title='Projet de Test',
            description='Description de test',
            start_date='2023-01-01',
            end_date='2023-12-31',
            status='DF',
            budget=10000.00,
            manager=self.user
        )
        self.project.team_members.add(self.user)

    def test_home_page_unauthorized(self):
        """Test l'accès à la page d'accueil sans authentification"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)  # Redirection vers login

    def test_home_page_authorized(self):
        """Test l'accès à la page d'accueil avec authentification"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Projet de Test')

    def test_project_detail_page(self):
        """Test la page de détail d'un projet"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('project-detail', args=[self.project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.project.title)
        self.assertContains(response, self.project.description)

    def test_create_project_form(self):
        """Test l'affichage du formulaire de création de projet"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('project-create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')

    def test_project_list_api(self):
        """Test l'API de liste des projets"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/api/projects/', HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Projet de Test')

    def test_project_detail_api(self):
        """Test l'API de détail d'un projet"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(f'/api/projects/{self.project.id}/', HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['title'], 'Projet de Test')
        self.assertEqual(data['status'], 'DF')

    def test_project_progress_api(self):
        """Test l'API de progression d'un projet"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(f'/api/projects/{self.project.id}/progress/', HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['progress'], 0.0)

    def test_project_create_api(self):
        """Test la création de projet via API"""
        self.client.login(username='testuser', password='testpass123')
        new_project = {
            'title': 'Nouveau Projet API',
            'description': 'Créé via API',
            'start_date': '2023-06-01',
            'end_date': '2023-12-31',
            'status': 'DF',
            'budget': 15000.00,
            'manager': self.user.id,
            'team_members': [self.user.id]
        }
        response = self.client.post(
            '/api/projects/',
            data=json.dumps(new_project),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Project.objects.count(), 2)