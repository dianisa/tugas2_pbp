from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.models import User
from django.core import serializers

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    context = {
    'nama': 'Dianisa Wulandari',
    'npm': 'NPM 2106702150',
    } 
    return render(request, "todolist_ajax.html", context)

def show_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')

    context = {}
    return render(request, 'login.html', context)

def show_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if username and password1 and password2:
            if password1 != password2:
                messages.info(request, 'Password berbeda!')
            else:
                try:
                    createUser = User.objects.create(username=username)
                    createUser.set_password(password1)
                    createUser.save()
                    messages.success(request, 'Akun telah berhasil dibuat!')
                    return redirect('todolist:show_login')
                except:
                    messages.info(request, 'Username sudah pernah digunakan!')
        else:
            messages.info(request, 'Semua harus terisi!')
    context = {}
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

def tambah_todolist(request):
    if request.method == 'POST':
        title = request.POST.get('get_title')
        description = request.POST.get('get_description')

        task_object = Task(user = request.user, title = title,\
                    date = datetime.date.today(), description = description)

        task_object.save()
        return render(request, 'todolist_ajax.html')
    return render(request, 'todolist_ajax.html')

def show_logout(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:show_login'))
    response.delete_cookie('last_login')
    return response

def show_todolist_json(request):
    data = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")