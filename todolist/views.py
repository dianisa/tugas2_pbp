from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = request.user
    data_todolist = Task.objects.all()

    context = {
        'to_do_list': data_todolist,
        'nama': 'Dianisa Wulandari',
        'npm': ' NPM 2106702150',
        'user': user
    }
    return render(request, "todolist.html", context)

def show_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')

    context = {}
    return render(request, 'login.html', context)

def show_register(request):
    form = forms.UserCreationForm()

    if request.method == "POST":
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:show_login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def show_create_task(request):
    if request.method == 'POST':
        get_title = request.POST.get('title')
        get_description = request.POST.get('description')
        task_object = Task(user = request.user, title = get_title,\
                    date = datetime.date.today(), description = get_description)
        task_object.save()
        messages.success(request, 'Task successfully added!')
        return redirect('todolist:show_todolist')

    context = {}
    return render(request, "create.html", context)

def show_logout(request):
    logout(request)
    return redirect('todolist:show_login')