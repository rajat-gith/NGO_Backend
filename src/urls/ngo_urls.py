
from django.urls import path
from src.views import ngo_views as views

urlpatterns=[
    path('add/',views.addNgo,name="ngoadd"),
    path('',views.getNgos,name="ngos"),
    path('<str:pk>/',views.getNgo,name="ngo"),
]