from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	context = RequestContext(request)
	return render_to_response('index.html', {}, context)

@login_required
def view1(request):
	context = RequestContext(request)
	return render_to_response('view1.html', {}, context)

@login_required
def view2(request):
	context = RequestContext(request)
	return render_to_response('view2.html', {}, context)

@login_required
def view3(request):
	context = RequestContext(request)
	return render_to_response('view3.html', {}, context)

