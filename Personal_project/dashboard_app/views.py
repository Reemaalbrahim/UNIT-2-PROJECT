from django.shortcuts import render, redirect
from experience_app.models import Experience
from projects_app.models import Project
from main_app.models import Message

def dashboard_view(request):
    experiences = Experience.objects.all().order_by('-start_date')
    projects = Project.objects.all()
    messages = Message.objects.all().order_by('-created_at')

    context = {
        'experiences': experiences,
        'projects': projects,
        'messages': messages,
    }
    return render(request, 'dashboard_app/dashboard.html', context)

def add_experience_view(request):
    if request.method == 'POST':
        # Handle form submission and create a new experience
        pass
    return render(request, 'dashboard_app/add_experience.html')

def edit_experience_view(request, experience_id):
    experience = Experience.objects.get(id=experience_id)
    if request.method == 'POST':
        # Handle form submission and update the experience
        pass
    return render(request, 'dashboard_app/edit_experience.html', {'experience': experience})

def delete_experience_view(request, experience_id):
    experience = Experience.objects.get(id=experience_id)
    if request.method == 'POST':
        # Handle form submission and delete the experience
        pass
    return render(request, 'dashboard_app/delete_experience.html', {'experience': experience})

def add_project_view(request):
    if request.method == 'POST':
        # Handle form submission and create a new project
        pass
    return render(request, 'dashboard_app/add_project.html')

def edit_project_view(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        # Handle form submission and update the project
        pass
    return render(request, 'dashboard_app/edit_project.html', {'project': project})

def delete_project_view(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        # Handle form submission and delete the project
        pass
    return render(request, 'dashboard_app/delete_project.html', {'project': project})
