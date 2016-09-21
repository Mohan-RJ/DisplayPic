"""ProfilePic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin, auth
from django.contrib.auth.views import *
from django.conf import settings

from ProfilePicApp.views import *

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^loginpage/', loginpage, name='loginpage'),
    url(r'^login/', auth.views.login, name='login'),
	url(r'^register/', register, name='register'),
    url(r'^home/', home, name='home'),
    url(r'^photoupload/', photoupload, name='photoupload'),
    url(r'^dashboard/', dashboard, name='dashboard'),
    url(r'^logout/', logout_page, name='logout_page'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', loginpage),
    url(r'^accounts/login/?next=/home/', loginpage),
]
