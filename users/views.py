from django.shortcuts import render
from .models import Profile
from django.shortcuts import render,redirect
from django.contrib import  messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUser
from django.contrib.auth import login,authenticate,logout

# Create your views here.


def loginUser(request):
    page = 'login'
    context={'page':page}

    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method=="POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        try:
            user= User.objects.get(username = username)
        except:
            messages.error(request,"Username does not exist")

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,"Username or password is incorrect")
            print("Username is incorrect")
        
    return render(request,'users/login_register.html',context)


def registerUser(request):
    page = 'register'
    form = CustomUser()
    if request.method=="POST":
        form = CustomUser(request.POST)
    
        if form.is_valid():
            user= form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,'User account created sucessfully')
            login(request,user)
            return redirect("profiles")
        
        else:

            messages.error(request,'Something wrong')
    context = {'page':page,'form':form}
    return render(request,'users/login_register.html',context)


def logoutUser(request):
    logout(request)
    messages.info(request,"User logged out")
    return redirect("login")

def profiles(request):
    profile= Profile.objects.all()
    context ={'profiles':profile}
    return render(request,'users/profile.html',context)


def user_profiles(request,pk):
    profile= Profile.objects.get(id=pk)
    skillsdesc = profile.skill_set.exclude(description__exact="")
    otherskills = profile.skill_set.filter(description="")
    context ={'profile':profile,'skillsdesc':skillsdesc,'otherskills':otherskills}

    return render(request,'users/user-profile.html',context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skillsdesc = profile.skill_set.all()
    projects= profile.project_set.all()
    context ={'profile':profile,'skillsdesc':skillsdesc,'projects':projects}
    return render(request,'users/account.html',context)
