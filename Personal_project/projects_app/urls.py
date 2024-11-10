from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list_view, name='project_list_view'),  
    path('add/', views.add_project_view, name='add_project_view'),  
]

