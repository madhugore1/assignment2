from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Todo
from django.http import JsonResponse
from django.template import RequestContext
# from .forms import TodoForm
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import HttpResponse

def login_redirect(request):
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('/todo_list/login')

def index(request):
    return render(request, 'todo_list/index.html')

@login_required
def home(request):
    todo_list = Todo.objects.order_by('id')
    user_todos = todo_list.filter(user = request.user)
    # form = TodoForm()
    context = {'todo_list': user_todos, 'user': request.user}
    return render(request, 'todo_list/home.html', context)

def addTodo(request):
    if request.method == 'POST':
        task = request.POST['task']
        user = request.user

        todo = Todo.objects.create(
            task = task,
            user = user
        )

        print(todo.id)

        return HttpResponse(todo.id)

def toggleTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.todo_bool = not todo.todo_bool
    todo.save()

    return HttpResponse('')

def deleteSelected(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()

    return HttpResponse('')

def editTodo(request, todo_id):
    if request.method == 'POST':
        task = request.POST['task']
        todo = Todo.objects.get(pk=todo_id)
        todo.task = task
        todo.save()

        data = {
            'todo_id': todo.id,
            'task': todo.task
        }

        return JsonResponse(data)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(
                request,
                username=username,
                password=password
            )
            login(request, user)
            return redirect('home')
        else:
            return redirect('register')

    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'todo_list/register.html', args)
