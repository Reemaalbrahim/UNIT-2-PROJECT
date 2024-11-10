from django.urls import path
from . import views

urlpatterns = [
    path('', views.experience_list_view, name='experience_list_view'),  
    path('add/', views.add_experience_view, name='add_experience_view'),  
]
