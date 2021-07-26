from django.urls import path
from . import views # dot means all. connecting views.py file

urlpatterns = [
    path('', views.index),  # views file wants to look into its file and dot is telling which function to go into the views. INdex is empty at this time. We will create that
    path('new', views.new),
    path('create', views.create),
    path('<int:number>', views.show),
    path('<int:number>/edit', views.edit),
    path('<int:number>/delete', views.destroy),
    path('me', views.myself),
    path('you/<str:name>', views.yourself)
]
