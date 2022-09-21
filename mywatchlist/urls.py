# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import *

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_mywatchlist_id, name='show_mywatchlist_id'),
    path('json/', show_mywatchlist_id, name='show_mywatchlist_id')
]