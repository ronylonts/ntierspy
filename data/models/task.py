from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .project import Project

class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = 'LO', 'Basse'
        MEDIUM = 'ME', 'Moyenne'
        HIGH = 'HI', 'Haute'
        CRITICAL = 'CR', 'Critique'

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    assigned_to = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )
    due_date = models.DateField()
    priority = models.CharField(
        max_length=2,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    is_completed = models.BooleanField(default=False)
    completion_percentage = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    depends_on = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='dependent_tasks'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['priority', 'due_date']
        verbose_name = 'Tâche'
        verbose_name_plural = 'Tâches'

    def __str__(self):
        return f"{self.title} ({self.project})"

    def save(self, *args, **kwargs):
        if self.completion_percentage == 100:
            self.is_completed = True
        super().save(*args, **kwargs)