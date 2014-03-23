from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
	context = RequestContext(request)
	return render_to_response('index.html', {}, context)

@login_required
def profile(request):
	context = RequestContext(request)
	return render_to_response('profile.html', {}, context)

def archive(request):
	context = RequestContext(request)
	return render_to_response('archive.html', {}, context)

def user(request, username):
	context = RequestContext(request)
	return render_to_response('user.html', {}, context)

def challenge(request, challenge_id):
	context = RequestContext(request)
	return render_to_response('challenge.html', {}, context)

def login(request):
	context = RequestContext(request)
	return render_to_response('index.html', {}, context)

def register(request):
	context = RequestContext(request)
	return render_to_response('index.html', {}, context)
