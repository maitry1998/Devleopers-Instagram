from django.urls import path
from . import views

urlpatterns = [
    path('',views.profiles,name="profiles"),
    path('userprofile/<str:pk>',views.user_profiles,name="user-profile"),
    path('login/',views.loginUser,name="login"),
    path('register/',views.registerUser,name="register"),
    path('logout/',views.logoutUser,name="logout"),
    path('account/',views.userAccount,name="account"),
    path('edit-account/',views.editAccount,name="edit-account"),
    path('create-skill/',views.createSkill,name="create-skill"),
    path('update-skill/<str:pk>',views.updateSkill,name="update-skill"),
    path('delete-skill/<str:pk>',views.deleteSkill,name="delete-skill"),
    path('inbox/',views.inbox,name="inbox"),
    path('message/<str:pk>',views.viewmessage,name="message"),
    path('send-message/<str:pk>/',views.createMessage,name="send-message"),
]