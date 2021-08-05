from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    # return HttpResponse("working")
    if 'count' in request.session:
        request.session['count'] += 1
        request.session['word'] = get_random_string(length=14)
    else:
        request.session['count'] = 0
        request.session['word'] = "  "
    return render(request, "random_word.html")


def generate(request):
    # request.session.flush()
    if 'count' in request.session:
        request.session['count'] += 1
        request.session['word'] = get_random_string(length=14)
        return render(request, 'random_word.html')
    else:
        redirect('/')

def flush(request):
    request.session.flush()
    return redirect('/')