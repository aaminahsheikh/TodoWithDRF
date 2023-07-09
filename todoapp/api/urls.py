from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_api),
    path('tasks/', views.TaskAPI.as_view()),
    #path('tasks/', views.GetTasks.as_view({'get': 'list'})),
]