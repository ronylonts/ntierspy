from django.db import models

class Project(models.Model):
    STATUS_CHOICES = [
        ('PL', 'Planning'),
        ('IP', 'In Progress'), 
        ('CO', 'Completed'),
        ('CA', 'Cancelled'),  # Notez la virgule à la fin
    ]
    budget = models.DecimalField(
    max_digits=10, 
    decimal_places=2,
    default=0.00  # ou null=True, blank=True
)
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=2, 
        choices=STATUS_CHOICES, 
        default='PL'
    )
    
    def __str__(self):
        return self.name