# TODO: Implement Routings Here
from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', show_register, name='show_register'),
    path('login/', show_login, name='show_login'),
    path('logout/', show_logout, name='show_logout'),
    path('logout/', show_logout, name='show_logout'),
    path('create-task/', show_create_task, name='show_create_task')
]