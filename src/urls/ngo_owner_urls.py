from django.urls import path
from src.views import ngoOwner_views as views


urlpatterns=[
    path('', views.getOwners, name='token_obtain_pair'),
    path('login/', views.MyTokenObtainPairViewOwner.as_view(), name='token_obtain_pair'),
    path('register/',views.registerOwner,name='register'),
]