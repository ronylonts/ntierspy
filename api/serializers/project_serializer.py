from rest_framework import serializers
from data.models import Project
from business.dtos import ProjectDTO

class ProjectSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()
    manager_name = serializers.CharField(source='manager.get_full_name', read_only=True)
    team_member_names = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'start_date', 'end_date',
            'status', 'budget', 'manager', 'manager_name', 'team_members',
            'team_member_names', 'created_at', 'updated_at', 'progress'
        ]
        extra_kwargs = {
            'manager': {'write_only': True},
            'team_members': {'write_only': True},
        }

    def get_progress(self, obj):
        return obj.progress

    def get_team_member_names(self, obj):
        return [member.get_full_name() for member in obj.team_members.all()]

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        return ProjectDTO(
            id=internal_value.get('id'),
            title=internal_value.get('title'),
            description=internal_value.get('description'),
            start_date=internal_value.get('start_date'),
            end_date=internal_value.get('end_date'),
            status=internal_value.get('status'),
            budget=internal_value.get('budget'),
            manager_id=internal_value.get('manager'),
            team_member_ids=data.get('team_members', []),
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['status_display'] = instance.get_status_display()
        return representation