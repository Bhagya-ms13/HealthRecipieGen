from django.urls import path 
from .views import BlogListView, BlogDetailView, BlogView

urlpatterns =[
    path('addpost/', BlogListView.as_view(), name='blog-list'),
    path('addpost/index',BlogView.as_view(), name='blog-detail'),
    
    path('addpost/<int:pk>',BlogDetailView.as_view(), name='blog-detail')
]