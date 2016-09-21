from django.shortcuts import render
import os
# Create your views here.
from ProfilePicApp.models import *
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.files.base import ContentFile

#============================#
#Custom functions starts here#
#============================#

#Index/Landing page.
def index(request):
	return render(request, 'registration/register.html')

#login function to authenticate the user if registered.
def loginpage(request):
	return render(request, 'registration/login.html')

#Save registration values of client to database
def register(request):
	if request.method == 'POST':
		base = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/ProfilePicApp/static/users/'
		body_unicode = request.body.decode('utf-8')
		content = json.loads(body_unicode)
		avatar = 'users/avatar.jpg'
		try:
			os.mkdir(os.path.join(base, content['username']))
			savedefaultpic = ProfilePics(username=content['username'], profilepic=avatar)
			savedefaultpic.save()
		except:
			pass
		try:
			checkuser = User.objects.get(username=content['username'])
		except:
			user = User.objects.create_user(
			username=content['username'],
			password=content['password'],
			email=content['email']
			)
			return HttpResponseRedirect('/')

	return render(request, 'registration/register.html')

#Homepage/Dashboard function which can be viewed by an authenticated user.
@login_required
def home(request):
	getpic = ProfilePics.objects.get(username=request.user)
	return render_to_response('dashboard/home.html', locals(), {'user': request.user})

@login_required
def dashboard(request):
	reg_users = User.objects.all()
	return render_to_response('dashboard/dashboard.html', locals())

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login')

#Function for uploading profile pictures.
@csrf_exempt
def photoupload(request):
    if request.user.is_authenticated():
         uname = str(request.user)
    uploaded_filename = request.FILES['file'].name
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/ProfilePicApp/static/users/'
    destination = 'users/' + uname +"/"+ uploaded_filename
    # save the uploaded file inside that folder.
    full_filename = os.path.join(base_path, uname, uploaded_filename)
    fout = open(full_filename, 'wb+')

    file_content = ContentFile( request.FILES['file'].read() )

    try:
        # Iterate through the chunks.
        for chunk in file_content.chunks():
            fout.write(chunk)
        fout.close()
        try:
        	savepic = ProfilePics.objects.get(username=uname)
        	savepic.profilepic = destination
        	savepic.save()
        except:
        	savepic = ProfilePics(username=uname, profilepic=destination)
        	savepic.save()
        return HttpResponseRedirect('/home')
    except:
        return HttpResponseRedirect('/home')