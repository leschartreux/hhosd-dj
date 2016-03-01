from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.redirects.models import Redirect

# Create your views here.

@login_required
def home(request):

    return render(request,'website/acceuil.html',{})

def edition(request):
    return render(request,'website/edition.html',{})

def exagroup(request):
    return render(request,'website/EXgroup.html',{})