from django.contrib import admin
from django.urls import path,include
from base import views 

urlpatterns = [
    path("", views.homepage), 
    path("admin/", admin.site.urls),
    path("api/ngos/",include('src.urls.ngo_urls')),
    path('api/users/',include('src.urls.donor_urls')),
]
