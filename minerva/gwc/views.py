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
