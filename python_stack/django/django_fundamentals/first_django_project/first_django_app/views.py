from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/")
def show(request, number):
    return HttpResponse(f"Placeholder to display blog number {number}.")

def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog {number}.")

def destroy(request, number):
    return redirect('/')


def myself(request):
    context = {
    "name": "Mina",
    "favorite_color": "white",
    "pets": ["Casper", "Junior", "Narda"]
    }
    return render(request, "hellodjango.html", context)

#CONTEXT dictionary which hold all variables going to be used in html. any keys you defined in this dictionary going to be variable name that you have in html
def yourself(request, name):
    context = {
        "htmlname":name,
        "namelist":["Alice","Bob","Charlie","David"]
    }   
    return render (request, "welcome.html", context) 