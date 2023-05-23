
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('profilec/', include('profilec.urls')),
    path('addpost/', include('addpost.urls'))
]
