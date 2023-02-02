from django.shortcuts import render, redirect
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_app/todo_list.html', {'todos': todos})

def todo_add(request):
    if request.method == 'POST':
        task = request.POST['task']
        todo = Todo(task=task)
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo_app/todo_add.html')

def todo_complete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todo_list')
