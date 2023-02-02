from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.todo_add, name='todo_add'),
    path('complete/<int:pk>/', views.todo_complete, name='todo_complete'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
]
