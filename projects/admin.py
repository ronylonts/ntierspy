from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'budget', 'status', 'is_active')
    list_filter = ('status', 'start_date')
    search_fields = ('name', 'description')
    date_hierarchy = 'start_date'
    ordering = ('-created_at',)