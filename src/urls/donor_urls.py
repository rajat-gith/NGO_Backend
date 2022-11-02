from django.urls import path
from src.views import donor_views as views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('donors/',views.getDonors,name="donors"),
    path('donors/<str:pk>/',views.getDonorById,name="donor"),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/',views.getUserProfile,name="user-profile"),
    path('profile/update/', views.updateUserProfile, name="user-profile-update"),
    path('',views.getUsers,name="users"),
    path('register/',views.registerUser,name='register')
]
