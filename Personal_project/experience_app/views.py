from django.shortcuts import render, redirect
from .models import Experience
from .forms import ExperienceForm  

def experience_list_view(request):
    experiences = Experience.objects.all()
    return render(request, 'experience_app/experience_list.html', {'experiences': experiences})

def add_experience_view(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experience_list')  
    else:
        form = ExperienceForm()
    return render(request, 'experience_app/add_experience.html', {'form': form})

