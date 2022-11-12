from django.contrib import admin
from django.urls import path,include
from base import views 

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



urlpatterns = [
    path("", views.homepage), 
    path("admin/", admin.site.urls),
    path("api/ngos/",include('src.urls.ngo_urls')),
    path('api/users/',include('src.urls.donor_urls')),
    path('api/ngoOwners/',include('src.urls.ngo_owner_urls')),
]
