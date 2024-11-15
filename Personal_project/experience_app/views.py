from django.shortcuts import render, redirect
from .models import Experience

def experience_list_view(request):
    experiences = Experience.objects.all()
    return render(request, 'experience_app/experience_list.html', {'experiences': experiences})

def add_experience_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        employment_type = request.POST.get('employment_type')
        company = request.POST.get('company')
        currently_working = 'currently_working' in request.POST
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date') or None
        location = request.POST.get('location')
        description = request.POST.get('description')

        experience = Experience.objects.create(
            title=title,
            employment_type=employment_type,
            company=company,
            currently_working=currently_working,
            start_date=start_date,
            end_date=end_date,
            location=location,
            description=description
        )
        experience.save()
        return redirect('experience_app:experience_list')
    return render(request, 'experience_app/add_experience.html')

