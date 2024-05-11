from django.urls import path

from todo_app.views import index, update, close, delete

urlpatterns = [
    path('', index, name='tasks'),
    path('update/<int:pk>/', update, name='task-update'),
    path('close/<int:pk>/', close, name='task-close'),
    path('delete/<int:pk>/', delete, name='task-delete'),
]
