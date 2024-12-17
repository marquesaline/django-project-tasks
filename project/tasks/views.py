from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
    else:
        form = TaskForm()
    return render(request, 'form_task.html', {'form': form})      

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks })

def get_task(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'task.html', {'task': task })

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'form_task.html', {'form': form})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('list_tasks')
