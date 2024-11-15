from django.urls import path
from . import views


app_name="education_app"

urlpatterns = [
    path('skills/', views.skills_view, name='skills_view'),  
]
