from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from todo_app.forms import TaskForm
from todo_app.models import Task


def index(request: WSGIRequest):
    form = TaskForm
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks")

    tasks = Task.objects.all().order_by('closed', '-updated_at', )
    context = {
        'tasks': tasks,
        'task_form': form
    }
    return render(request, template_name='todo_app/index.html', context=context)


def update(request: WSGIRequest, pk: int):
    task = Task.objects.get(pk=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    context = {
        "edit_form": form
    }
    return render(request, "todo_app/update.html", context)


def close(request: WSGIRequest, pk: int):
    task = Task.objects.get(pk=pk)
    task.closed = True
    task.save()
    return redirect("tasks")


def delete(request: WSGIRequest, pk: int):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect("tasks")
    context = {
        'task': task
    }
    return render(request, "todo_app/delete.html", context)
