from django.urls import path
from . import views

app_name = 'dashboard_app'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard_view'),
    path('experience/add/', views.add_experience_view, name='add_experience_view'),
    path('experience/<int:experience_id>/edit/', views.edit_experience_view, name='edit_experience_view'),
    path('experience/<int:experience_id>/delete/', views.delete_experience_view, name='delete_experience_view'),
    path('project/add/', views.add_project_view, name='add_project_view'),
    path('project/<int:project_id>/edit/', views.edit_project_view, name='edit_project_view'),
    path('project/<int:project_id>/delete/', views.delete_project_view, name='delete_project_view'),
]

