from django.urls import path

from base_app import views


app_name = 'base_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/<int:project_id>/', views.projects, name='projects'),
    path('quiz_handler/', views.quiz_handler, name='quiz_handler'),
    path('consult_handler/', views.consult_handler, name='consult_handler'),
]
