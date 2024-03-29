from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,Tag
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProjects
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .utils import paginateProjects

# Create your views here.
def projects(request):
    projects,search_query= searchProjects(request)
    results=3
    custom_range, projects= paginateProjects(request,projects,results)
    



    context = { 'projects':projects,'search_query':search_query,'custom_range':custom_range}
    return render(request,'projects/projects.html',context)


@login_required(login_url="login")
def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    return render(request,'projects/single-project.html',{'project':projectObj})


@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()
    context = {'form':form }
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user.profile
            project.save()
            return redirect('account')
    return render(request,'projects/project_form.html',context)

@login_required(login_url="login")
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    # project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    context = {'form':form }
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    return render(request,'projects/project_form.html',context)


@login_required(login_url="login")
def deleteProject(request,pk):
    profile = request.user.profile
    project= profile.project_set.get(id=pk)
    context ={'object':project}
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    return render(request,'delete_object.html',context)

