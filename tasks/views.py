from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render

# Partie API DRF
class TaskListAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Protection JWT

class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

# Partie Template (si nécessaire)
def task_list_view(request):
    return render(request, 'tasks/list.html')

def task_create_view(request):
    return render(request, 'tasks/create.html')

def task_detail_view(request, task_id):
    return render(request, 'tasks/detail.html', {'task_id': task_id})