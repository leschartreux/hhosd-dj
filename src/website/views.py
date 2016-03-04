from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.redirects.models import Redirect
from django.http.request import HttpRequest
from django.http import *
from website.models import Machine
from collections import namedtuple
from django.db import connections

# Create your views here.
# @login_required(login_url='/login/') -> add this field above every views which requires to be logged in, in order to be accessed
def fetchallmachine(cursor):
    desc=cursor.description
    nt_result = [col[0] for col in desc]
    return [dict(zip(nt_result,row)) for row in cursor.fetchall()]

@login_required(login_url='/login/')
def home(request):
    
    cursor = connections['postes'].cursor()
    cursor.execute("SELECT * FROM MACHINE WHERE pyddlaj=1");
    result = fetchallmachine(cursor)
        
    return render(request,'website/acceuil.html',result)

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



