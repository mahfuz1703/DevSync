from django.contrib import admin
from django.urls import path, include
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('add/', TaskCreate.as_view(), name='createTask'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='updateTask'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='deleteTask'),

]