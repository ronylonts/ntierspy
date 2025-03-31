from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project
from .forms import ProjectForm

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/list.html'
    context_object_name = 'projects'
    paginate_by = 10

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/detail.html'

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/create.html'
    success_url = '/projects/'

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/update.html'
    success_url = '/projects/'

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/delete.html'
    success_url = '/projects/'

# Ajoutez cette fonction view si vous voulez garder l'approche fonctionnelle
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/list.html', {'projects': projects})