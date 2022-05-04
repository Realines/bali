from django.urls import path

from projects import views


app_name = 'projects'

urlpatterns = [
    path('<int:project_id>/', views.projects, name='projects'),
    # path('project-paginator/', views.projects_paginator,
    #      name='project_paginator'),
]
