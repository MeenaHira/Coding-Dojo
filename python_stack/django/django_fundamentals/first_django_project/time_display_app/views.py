from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

# Create your views here.
# def index(request):
#     return HttpResponse (strftime("%b %m, %Y  %I:%M %p", gmtime()))

def index(request):
    context = {
        "time": strftime("%b %d, %Y  %I:%M %p", gmtime())
    }
    return render(request, 'index.html', context)

def date_time (request):
    context ={
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%I:%M %p", gmtime())
    }
    return render (request, 'index.html', context)