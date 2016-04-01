"""maquette URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home') 
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from website import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'$^', views.home,name = "home"),
    url(r'^edition/?$',views.edition,name ="edition"),
    url(r'^exaGroup/?$',views.exagroup,name = "group"),
    url(r'^exaComputer/?$',views.exagroup,name="test"),
    
    url(r'^taskGroup1/$',views.taskGroup1,name ="taskGroup1"),
    url(r'^taskGroup2/?$',views.taskGroup2,name ="taskGroup2"),
    
    url(r'^login/?$', views.login_user)

    
] 

# Static files are accessed only during the development phase // Les fichiers staitc ne sont accessibles que durant la phase de developpement
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)