# In views.py
from django.shortcuts import render, redirect


def skills_view(request):
    return render(request, 'education_app/skills.html')  # Render the skills.html template

