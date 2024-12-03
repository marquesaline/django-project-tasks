from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            form = TaskForm()
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})      

