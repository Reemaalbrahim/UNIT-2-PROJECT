from django.urls import path
from . import views

app_name="experience_app"

urlpatterns = [
    path('', views.experience_list_view, name='experience_list_view'),  
    path('add/', views.add_experience_view, name='add_experience_view'),  
]
