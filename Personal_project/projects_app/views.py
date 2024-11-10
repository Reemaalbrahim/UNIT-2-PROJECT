from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm  

def project_list_view(request):
    projects = Project.objects.all()
    return render(request, 'project_app/project_list.html', {'projects': projects})

def add_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('project_list') 
    else:
        form = ProjectForm()
    return render(request, 'project_app/add_project.html', {'form': form})

