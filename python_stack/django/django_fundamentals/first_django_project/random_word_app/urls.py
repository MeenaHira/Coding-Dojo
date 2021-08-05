from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index), 
    path('generate', views.generate),
    path('flush', views.flush)
]
