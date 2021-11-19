from django.urls import path

from base_app import views


app_name = 'base_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/<int:project_id>/', views.projects, name='projects'),
]
