from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.redirects.models import Redirect
from django.http.request import HttpRequest
from django.http import *
from collections import namedtuple
from django.db import connections
from django.views.generic import ListView
from django.core import serializers
import json

"""
def fetchallmachine(cursor):
    desc=cursor.description
    nt_result = [col[0] for col in desc]
    return [dict(zip(nt_result,row)) for row in cursor.fetchall()]
"""
# Create your views here.
# @login_required(login_url='/login/') -> add this field above every views which requires to be logged in, in order to be accessed
@login_required(login_url='/login/')
def home(request):
    
    cursor = connections['hhosd_ng'].cursor()
    cursor.execute("SELECT cmp.name,cmp.ip,cmp.mac,model_vendor,model_name FROM computer cmp, computermodel cmpm WHERE is_hhosd=1 AND cmp.model_id = cmpm.model_id ORDER BY cmp.name");
    computerList = cursor.fetchall()
    cursor.execute("SELECT * FROM hhosd_ng.partition")
    test = cursor.fetchall()
    cursor.execute("SELECT * FROM hhosd_ng.masterimage")
    test2 = cursor.fetchall()
    
    return render_to_response('website/acceuil.html',{'computerList':computerList,'test':test,'test2':test2},context_instance=RequestContext(request))

@login_required(login_url='/login/')
def edition(request):
    return render(request,'website/edition.html')

@login_required(login_url='/login/')
def exagroup(request):
    return render(request,'website/EXgroup.html')

@login_required(login_url='/login/')
def taskGroup1(request):
    cursor = connections['hhosd_ng'].cursor()
    cursor.execute("SELECT grp.name FROM hhosd_ng.group grp")
    groupNameList = cursor.fetchall()
    cursor.execute("SELECT name FROM task_type")
    taskNameList = cursor.fetchall()     
    return render_to_response('website/taskGroup1.html',{'groupNameList':groupNameList,'taskNameList':taskNameList},context_instance=RequestContext(request))

def taskGroup2(request):
    gname=request.POST['groups']
    cursor = connections['hhosd_ng'].cursor()
    cursor.execute("SELECT masterimage_id,name FROM masterimage ")
    masterList = cursor.fetchall()
    cursor.execute("SELECT mimg.*,mp.*,os.os_name FROM masterimage mimg,masterpartition mp, os WHERE mimg.masterimage_id=mp.masterimage_id AND mimg.os_id=os.os_id ORDER BY mimg.masterimage_id") 
    infoQuery = cursor.fetchall()
    masterJSON = json.dumps(infoQuery)
    cursor.execute("SELECT cmp.name FROM computer cmp,computer_group cmpg, hhosd_ng.group grp WHERE cmp.comp_id=cmpg.comp_id AND cmpg.group_id=grp.group_id AND grp.name='"+gname+"' ORDER BY cmp.name")
    compList = cursor.fetchall()  
    return render_to_response('website/taskGroup2.html',{'compList':compList,'masterList':masterList,'masterJSON':masterJSON},context_instance=RequestContext(request))


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



