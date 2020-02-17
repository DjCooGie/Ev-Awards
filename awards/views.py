from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.conf import settings
from django.templatetags.static import static
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
import datetime as dt
from django.contrib import messages
from .models import *
from .forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer


# Create your views here.
def home(request):
    date = dt.date.today()
    projects = Project.get_projects()
    
    return render(request, 'index.html', {"date": date, "projects":projects})



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created successfully')
            return redirect('/')
        
    else:
        form = RegisterForm()
    return render(request, 'registration/registration_form.html', {'form':form})

@login_required(login_url='/accounts/login/')
def user_profiles(request):
    current_user = request.user
    Author = current_user
    projects = Project.get_by_author(Author)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile')
        
    else:
        form = ProfileUpdateForm()
    
    return render(request, 'registration/profile.html', {"form":form})

