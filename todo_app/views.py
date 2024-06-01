from rest_framework import viewsets

from todo_app.models import Task
from todo_app.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
