from django.shortcuts import render, redirect
from experience_app.models import Experience
from projects_app.models import Project
from main_app.models import Message
from django.http import HttpRequest, HttpResponse

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

def edit_experience_view(request:HttpRequest, experience_id:int):
    experience = Experience.objects.get(id=experience_id)
    if request.method == 'POST':
        experience.title=request.POST["title"]
        experience.employment_type=request.POST["employment_type"]
        experience.company=request.POST["company"]
        experience.currently_working = request.POST.get("currently_working", False)
        experience.start_date=request.POST["start_date"]
        experience.end_date=request.POST["end_date"]
        experience.location=request.POST["location"]
        experience.description=request.POST["description"]
        experience.save()
   
    return render(request, 'dashboard_app/edit_experience.html', {'experience': experience})

def delete_experience_view(request:HttpRequest, experience_id:int):
    experience = Experience.objects.get(id=experience_id)
    experience.delete()

    return redirect("main_app:home_view")


def edit_project_view(request:HttpRequest, project_id:int):

    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        project.title=request.POST["title"]
        project.description=request.POST["description"]

        if "image" in request.FILES:
            project.image=request.FILES["image"]

        project.save()

    return render(request, 'dashboard_app/edit_project.html', {'project': project})

def delete_project_view(request:HttpRequest, project_id:int):

    project = Project.objects.get(id=project_id)
    project.delete()

    return redirect("main_app:home_view")
    

    