from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.redirects.models import Redirect
from django.http.request import HttpRequest
from django.http import *

# Create your views here.
# @login_required(login_url='/login/') -> add this field above every views which requires to be logged in, in order to be accessed

@login_required(login_url='/login/')
def home(request):    
    return render(request,'website/acceuil.html')

@login_required(login_url='/login/')
def edition(request):
    return render(request,'website/edition.html')

@login_required(login_url='/login/')
def exagroup(request):
    return render(request,'website/EXgroup.html')

def login_user(request):
    logout(request)
    username=password=''
    
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
    
    return render_to_response('website/login.html',context_instance=RequestContext(request))



