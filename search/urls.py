from django.urls import path 
from . import views
# from .views import SearchView
urlpatterns =[
    path('search', views.getval, name='search'),
    
]