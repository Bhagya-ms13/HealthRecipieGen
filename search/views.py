from django.http import HttpResponse
from django.template import loader
from addpost.models import Blog
from django.shortcuts import render
from django.views import View

        
def getval(request):
    context = {
        'blog_list' : "",
        'name': request.user



    }
    if(request.method == "POST"):
        diet = request.POST.get('diet')
        course = request.POST.get('course')
        print(diet)
        blogs = Blog.objects.filter(diet=diet, course = course)
            
        context = {
            'blog_list' : blogs,
            
            'name': request.user
        }
        return render(request, 'search/index.html', context)
    return render(request, 'search/index.html', context)
        
    
   