from django.urls import path
from . import views

urlpatterns = [
    path('', views.education_list_view, name='education_list_view'),
    path('add/', views.add_education_view, name='add_education_view'),
    path('skills/', views.skills_view, name='skills_view'),  
]
