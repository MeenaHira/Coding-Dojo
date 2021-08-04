from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

def index(request):
    # return HttpResponse("working")
    return render(request, "form.html")

def process(request):
    # print(request.POST) 
    # return HttpResponse("check my data in terminal")
    # return render(request, "result.html")
    if request.method == "POST":
        print(request.POST)
        context = {
            'name': request.POST['name'],
            'gen': request.POST['Gender'],
            'lang':request.POST['languages'],
            'loc':request.POST['location'],
            'comment':request.POST['comment']
        }
        # request.session['name']= request.POST['name'] #- e.g. add if requesting session data for nameve whole context directory will be deleted (by Chris)
        return render(request, "result.html", context) #- e.g. add if you don't redirect to new(empty HTML form) page(Chris)
        # return redirect('/new') # redirecting to new empty HTML form page


# def new(request):
#     # print('got here from redirect!')
#     # return redirect('/new')
#     return render(request, 'result.html')


# method result storing session data
def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request, 'result.html', context)

def new(request): #have to figure out how to redirect to index through process submit button without this method
    if request.method == "GET":
        print(request.POST)
        return redirect('/new')

#To use session data. Session dictinary to which we can add and retrieve values via keys
def data(request):
    request.session['counter']= 5
