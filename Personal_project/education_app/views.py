# In views.py
from django.shortcuts import render, redirect
from .models import Education

def education_list_view(request):
    educations = Education.objects.all()
    return render(request, 'education_app/education_list.html', {'educations': educations})

def add_education_view(request):
    if request.method == 'POST':
        education = Education(
            school=request.POST['school'],
            degree=request.POST['degree'],
            field_of_study=request.POST['field_of_study'],
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
            grade=request.POST.get('grade', ''),
            description=request.POST.get('description', '')
        )
        education.save()
        return redirect('education_list_view')  # Ensure this matches the name in urls.py

    return render(request, 'education_app/add_education.html')

def skills_view(request):
    return render(request, 'education_app/skills.html')  # Render the skills.html template

