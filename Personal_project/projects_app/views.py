from django.shortcuts import render, redirect
from .models import Project
from django.http import HttpRequest, HttpResponse

def project_list_view(request):
    projects = Project.objects.all()
    return render(request, 'projects_app/project_list.html', {'projects': projects})

def add_project_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['image']
        description = request.POST['description']
        project = Project.objects.create(title=title, image=image, description=description)
        project.save()
        return redirect('projects_app:project_list_view')
    return render(request, 'projects_app/add_project.html')


def publications_view(request):

    return render(request, 'projects_app/publications.html')


def project_detail_view(request:HttpRequest, project_id:int):

    project=Project.objects.get(pk=project_id)

    return render(request, 'projects_app/project_detail.html', {"project":project})




