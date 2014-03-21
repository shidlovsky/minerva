from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from authentication.forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


from django.core.mail import send_mail

def user_login(request):
	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse("Sorry, your account is disabled.")
		else:
			return render_to_response('authentication/login.html', {'error': True, 'username': username}, context)

	else:
		return render_to_response('authentication/login.html', {}, context)

def register(request):
	context = RequestContext(request)

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()

			new_user = authenticate(username=request.POST['username'], password=request.POST['password'])
			login(request, new_user)

			registered = True

			return HttpResponseRedirect('/')
		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render_to_response(
			'authentication/register.html',
			{'user_form': user_form, 'profile_form': profile_form},
			context)	

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')