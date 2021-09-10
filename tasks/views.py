from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
# Create your views here.

@login_required(login_url='login')
def index(request):
  user = request.user
  tasks = Task.objects.filter(user=user)

  form = TaskForm()

  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = user
        task.save()
    return redirect('/')

  context = {
    'tasks':tasks,
    'form': form,
  }
  return render(request, 'tasks/list.html', context)

@login_required(login_url='login')
def updateTask(request, pk):
  task=Task.objects.get(id=pk)

  form = TaskForm(instance=task)
  if request.method == 'POST':
    form=TaskForm(request.POST, instance=task)
    if form.is_valid():
      form.save()
    return redirect('/')
  
  context={'form': form}

  return render(request, 'tasks/update_task.html', context)

@login_required(login_url='login')
def deleteTask(request, pk):
  item = Task.objects.get(id=pk)
  if request.method == 'POST':
    item.delete()
    return redirect('/')
  context = {'item': item}
  return render(request, 'tasks/delete.html', context)

def loginUser(request):
  page = 'login'
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request, user)
      return redirect('list')
  context = {
    'page': page,
  }
  return render(request, 'tasks/login_register.html', context)

def logoutUser(request):
  logout(request)
  return redirect('login')

def registerUser(request):
  page = 'register'
  form  = CustomUserCreationForm()

  if request.method == 'POST':
    form  = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.save()

      user = authenticate(request, username=user.username, password=request.POST['password1'])

      if user is not None:
        login(request, user)
        return redirect('list')

  context = {
    'form': form,
    'page': page,
  }
  return render(request, 'tasks/login_register.html', context )
