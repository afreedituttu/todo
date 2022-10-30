from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import tasks
# Create your views here.

def home(request):
    if request.method=='POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username,password=password)
      if user is not None:
          login(request, user)
          return redirect('/')
      else:
          return redirect('/')
    else:
       task = tasks.objects.filter(completed=True)
       completedtask = tasks.objects.filter(completed=False)
       print(task)
       print(completedtask)
       content = {
        'task': completedtask,
        'ctask':task
       }
       return render(request,'index.html',{'content' : content })

    
def add(request):
    if request.user.is_authenticated:
        if request.method=='POST':
         name = request.POST['name']
         money = request.POST['money']
         task = tasks(name=name,money=money)
         task.save()
         return redirect('/')
        else:
         return render(request,'add.html')
    else:
        return redirect('/')
    

def complete(request, id):
    pass

def delete(request, id):
    tasks.objects.get(pk=id).delete()
    return redirect('/')

def complete(request, id):
    tasks.objects.filter(pk=id).update(completed=True)
    return redirect('/')

def logoutu(request):
    logout(request)
    return redirect('/')

def completedelete(request, id):
    tasks.objects.filter(pk=id).update(completed=False)
    return redirect('/')