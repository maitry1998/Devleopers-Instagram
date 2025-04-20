from django.shortcuts import render
from .models import Profile,Skill,Message
from django.shortcuts import render,redirect
from django.contrib import  messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUser, ProfileForm, SkillForm, MessageForm
from django.contrib.auth import login,authenticate,logout
from django.db.models import Q
from .utils import searchProfiles,paginateProfiles
# Create your views here.


def loginUser(request):
    page = 'login'
    context={'page':page}

    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method=="POST":
        username= request.POST.get("username").lower()
        password= request.POST.get("password")
        try:
            user= User.objects.get(username = username)
        except:
            messages.error(request,"Username does not exist")

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            # the next attribute here is next from adding a comment for un authenticated user
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
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
            return redirect("edit-account")
        
        else:
            messages.error(request,'Something wrong')
    context = {'page':page,'form':form}
    return render(request,'users/login_register.html',context)


def logoutUser(request):
    logout(request)
    messages.info(request,"User logged out")
    return redirect("login")

def profiles(request):
    profiles,search_query = searchProfiles(request)
    # profile= Profile.objects.all()
    results=2
    custom_range, profiles= paginateProfiles(request,profiles,results)
    
    context ={'profiles':profiles,'search_query':search_query,'custom_range':custom_range}
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

@login_required(login_url='login')
def editAccount(request):
    form = ProfileForm(instance=request.user.profile)
    context ={'form':form}

    if request.method == "POST":
        form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("account")
    return render(request,'users/profile_form.html',context)

@login_required(login_url = "login")
def createSkill(request):
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill=form.save(commit=False)
            skill.owner= request.user.profile
            skill.save()
            messages.success(request,"Skill was added successfully")
            return redirect('account')
    context={'form':form}

    return render(request,'users/skill_form.html',context)

@login_required(login_url = "login")
def updateSkill(request,pk):
    skill = request.user.profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == "POST":
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid():
            
            form.save()
            messages.success(request,"Skill was updated successfully")
            return redirect('account')
    context={'form':form}

    return render(request,'users/skill_form.html',context)


@login_required(login_url="login")
def deleteSkill(request,pk):
    profile = request.user.profile
    skill= profile.skill_set.get(id=pk)
    context ={'object':skill}
    if request.method == 'POST':
        skill.delete()
        messages.success(request,"Skill was deleted successfully")
        return redirect('account')
    return render(request,'delete_object.html',context)



@login_required(login_url="login")
def inbox(request):
    profile = request.user.profile

    #messagerequest has all messages for this profile
    messagerequest = profile.messages.all() #due to related name in models py file
    unread_count = messagerequest.filter(is_read=False).count()
    context = {'messagerequest':messagerequest,'unread_count':unread_count}
    return render(request,'users/inbox.html',context)

@login_required(login_url="login")
def viewmessage(request,pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk) #due to related name in models py file
    if message.is_read == False:
        message.is_read = True
        message.save()
    context={'message':message}
    return render(request,'users/message.html',context)


def createMessage(request,pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    try:
        sender= request.user.profile
    except:
        sender = None
    if request.method=="POST":
        form= MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender =sender
            message.recipient = recipient

            # this if statement is when user is logged in, we want to take the name and email id as the registerd email and name
            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request,"Your message was successfully sent!")
            return redirect("user-profile",pk)
    context={'recipient':recipient,'form':form}
    return render(request,'users/message_form.html',context)


