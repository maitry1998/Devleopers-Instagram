from django.urls import path
from . import views

urlpatterns = [
    path('',views.profiles,name="profiles"),
    path('userprofile/<str:pk>',views.user_profiles,name="user-profile"),
    path('login/',views.loginUser,name="login"),
    path('register/',views.registerUser,name="register"),
    path('logout/',views.logoutUser,name="logout"),
    path('account/',views.userAccount,name="account"),
]