from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator

class Project(models.Model):
    STATUS_CHOICES = [
        ('PL', 'Planning'),
        ('IP', 'In Progress'),
        ('CO', 'Completed'),
        ('CA', 'Cancelled'),
    ]
    
    name = models.CharField(
        max_length=100,
        verbose_name="Project Name",
        help_text="Enter the project name (max 100 characters)"
    )
    
    description = models.TextField(
        verbose_name="Description",
        help_text="Detailed description of the project"
    )
    
    start_date = models.DateField(
        verbose_name="Start Date",
        help_text="Project start date"
    )
    
    end_date = models.DateField(
        verbose_name="End Date",
        help_text="Project end date"
    )
    
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Budget",
        help_text="Project budget in dollars"
    )
    
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='PL',
        verbose_name="Status",
        help_text="Current project status"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Updated"
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})
    
    @property
    def duration(self):
        """Calculate project duration in days"""
        if self.start_date and self.end_date:
            return (self.end_date - self.start_date).days
        return 0
    
    @property
    def is_active(self):
        """Check if project is currently active"""
        return self.status == 'IP'