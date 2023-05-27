from django.urls import path 
from .views import BlogListView,  BlogView

urlpatterns =[
    path('addpost', BlogListView.as_view(), name='blog-list'),
    path('addpost/index',BlogView.as_view(), name='blog-detail'),
    
]