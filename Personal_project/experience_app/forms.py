from django import forms
from .models import Experience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'employment_type', 'company', 'currently_working', 'start_date', 'end_date', 'location', 'description']
