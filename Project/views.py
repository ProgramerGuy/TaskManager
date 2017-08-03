from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import (login as auth_login,  authenticate)
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from UserProfile.models import Profile, TypeOfUser
import datetime

def index(request):
	template = loader.get_template('index.html')
	context = {
	}
	return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def profile(request):
	template = loader.get_template('profile.html')
	context = {
	}
	return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def projects(request):
	template = loader.get_template('projects.html')
	profile = Profile.objects.filter(user=request.user)
	projects = Project.objects.filter(user=profile)
	context = {
		"Projects" : projects
	}
	return HttpResponse(template.render(context, request))

def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            us = form.save()
            user = Profile(user = us, userType = TypeOfUser.objects.all()[0])
            user.save()
            return redirect(reverse('Project:login'))
        else:
            print(form.errors)
    return render(request, 'sign_up.html', {'form': form})

def login(request):
	template = loader.get_template('login.html')
	_message = 'Please sign in'
	_username = ""
	_password = ""
	context = {}

	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('Project:projects'))
	if request.method == 'POST':
		_username = request.POST.get("username", "")
		_password = request.POST.get("password", "")
		user = authenticate(username=_username, password=_password )
		if user is not None:
			if user.is_active:
			    auth_login(request, user)
			    return HttpResponseRedirect(reverse('Project:projects'))
			else:
			    _message = 'Your account is not activated'
		else:
		    _message = 'Login Invalido, Intente de nuevo.'
		context = {'message': _message}
	return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def create_project(request):
	profile = get_object_or_404(Profile, user=request.user)
	form = ProjectForm()
	if request.method == 'POST':
		data = request.POST
		form = ProjectForm(data=data)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = profile
			post.save()
			form.save_m2m()
			return redirect(reverse('Project:projects'))
		else:
		    print(form.errors)
	return render(request, 'createProjects.html', {'form': form})

@login_required(login_url='/login/')
def create_task(request,pk):
	project = Project.objects.get(id=pk)
	form = TaskForm()
	if request.method == 'POST':
		data = request.POST
		form = TaskForm(data=data)
		if form.is_valid():
			post = form.save(commit=False)
			post.created_date = datetime.datetime.now()
			post.notify = False
			post.save()
			form.save_m2m()
			project.tasks.add(post)
			project.save()
			return redirect(reverse('Project:project_detail',kwargs={'pk':pk}))
		else:
		    print(form.errors)
	return render(request, 'createTask.html', {'form': form})

@login_required(login_url='/login/')
def project_detail(request,pk):
	profile = Profile.objects.get(user=request.user)
	project = Project.objects.get(id=pk)
	tasks = Task.objects.filter(project = project)
	print("Taks {0}".format(tasks))
	template = loader.get_template('project_detail.html')
	data = {
		'tasks':tasks, 
		'project': pk
	}
	return HttpResponse(template.render(data,request))