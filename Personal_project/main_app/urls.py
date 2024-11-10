from . import views
from django.urls import path

app_name = "main_app"

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('messages/', views.messages_view, name='messages_view'),
    path('resume/', views.resume_view, name='resume_view'),
]
