from typing import ContextManager
from django.shortcuts import render,redirect, HttpResponse
#instead of adding values for labels in form.html page we are adding LOCATIONS and LANGUAGES as a list from views.py through index method into html weppage 

LOCATIONS = (
    '--',
    'Bellevue, WA',
    'Boise, ID',
    'Chicago, IL',
    'Dallas, TX',
    'Los Angeles, CA',
    'Silicon Valley, CA',
    'Online'
)
LANGUAGES = (
    '--',
    'JavaScript',
    'Python',
    'C#',
    'Java'
)


# Create your views here.
#method index to bring html template to browser. passing list of values to variables as defined above
def index(request):
    # return HttpResponse("working")
    context = {
        'locations': LOCATIONS,
        'languages': LANGUAGES
    }
#adding page views to session counter.when we load the page it'll setup to counter
    if 'pageviews' in request.session:
        request.session['pageviews'] += 1
    else:
        request.session['pageviews'] = 0   
    return render(request, "form.html", context)

#method survey to GET information input from user and redirect to result page
def survey(request):
    print(request.POST) 
    # return HttpResponse("check my data in terminal")  
    # ---> checking if data from form.html goes to TERMINAL just with first two commands print and return above. In browser it shows Httpresponse statement"check my data in terminal" and in TERMINAL window it shows query dictionary(<QueryDict: {'csrfmiddlewaretoken': CSRF token['OuAdQsbH4Niml2XiHqraAeJH6QtvETgDzVyfAjStN6nbYsWUzzz0kpTRerqbTrne'], 'name': ['Meena Hira'], 'location': ['Bellevue, WA'], 'language': ['JavaScript'], 'comment': ['aua s y']}>[04/Aug/2021 03:08:18] "POST /survey HTTP/1.1" 200 25) 
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    print(request.session)
    # return HttpResponse("check my data in terminal") # Terminal won't show key and values as in dictionary when we checked data before in begining of this survey method. IN terminal it shows as (<django.contrib.sessions.backends.db.SessionStore object at 0x10d057a30>)
    return redirect('/result') # we are not using "return render(request, 'result.html', context)", instead we are redirecting to result method(empty HTML form)through below result method


# method result storing session data for security concerns. we don't want to process and render method in above 'survey method' to allow users to change individual values like comments, location etc.
def result(request):
    context = {
        'name': request.session['name'],
        'location' : request.session['location'],
        'language' : request.session['language'],
        'comment' : request.session['comment']
    }
    if 'pageviews' in request.session:
        request.session['pageviews'] += 1
        return render(request, 'result.html')
    else:
        redirect('/')

def flush(request):
    request.session.flush()
    return redirect('/')
