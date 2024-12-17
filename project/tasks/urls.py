from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.create_task, name='create_task'),
    path('', views.list_tasks, name='list_tasks'),
    path('<int:id>/', views.get_task, name='get_task'),
    path('atualizar/<int:id>/', views.update_task, name='update_task'),
    path('deletar/<int:id>/', views.delete_task, name='delete_task'),


]