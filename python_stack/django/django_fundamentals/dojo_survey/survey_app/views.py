from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("working")
    return render(request, "form.html")

def process(request):
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
        return render(request, "result.html", context)
    # return redirect('/')
    if request.method == "GET":
        return redirect('/')
    return render(request, "form.html") 


def new(request):
    print('got here from redirect!')
    return render(request, 'form.html')

# def new(request): #have to figure out how to redirect to index through process submit button without this method
#     # if request.method == "GET":
#     #     print(request.POST)
#         return redirect('/')
    