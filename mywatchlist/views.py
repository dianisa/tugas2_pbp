from email import message
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()

    # membandingkan jumlah film yang sudah ditonton dan belum ditonton
    num_watched = 0
    num_not_watched = 0
    message = "Wah, kamu masih sedikit menonton!"

    for movie in data_mywatchlist:
        if movie.watched:
            num_watched += 1
        else:
            num_not_watched += 1

    if num_watched >= num_not_watched:
        message = "Selamat, kamu sudah banyak menonton!"

    # context
    context = {
        'watch_list': data_mywatchlist,
        'nama': 'Dianisa Wulandari',
        'npm': '2106702150',
        'message': message
    }
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_json_xml(request):
    data = MyWatchList.objects.all()
    
    if ("json" in request.path):
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    elif ("xml" in request.path):
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
