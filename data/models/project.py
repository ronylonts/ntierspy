from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Brouillon'
        ACTIVE = 'AC', 'Actif'
        ON_HOLD = 'OH', 'En attente'
        COMPLETED = 'CO', 'Terminé'
        CANCELLED = 'CA', 'Annulé'

    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    manager = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='managed_projects'
    )
    team_members = models.ManyToManyField(
        User,
        related_name='projects',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'

    def __str__(self):
        return self.title

    @property
    def progress(self):
        """Calcule la progression du projet en fonction des tâches"""
        tasks = self.tasks.all()
        if not tasks:
            return 0
        total = len(tasks)
        completed = len([t for t in tasks if t.is_completed])
        return round((completed / total) * 100, 2)