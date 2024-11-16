from django.urls import path
from . import views

app_name = "projects_app"

urlpatterns = [
    path('', views.project_list_view, name='project_list_view'),
    path('add/', views.add_project_view, name='add_project_view'),
    path('publications/', views.publications_view, name='publications_view'),
    path('detail/<project_id>/', views.project_detail_view, name='project_detail_view'),
    
]


