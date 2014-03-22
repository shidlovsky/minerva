from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json
from app.models import *

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

@login_required
def appliance_classes(request):
	context = RequestContext(request)
	classes = ApplianceClass.objects.all()
	res = []
	for x in classes:
		res.append(x.name)

	return HttpResponse(json.dumps(res), content_type="application/json")

@login_required
def appliance_types(request, appliance_class):
	context = RequestContext(request)
	types = ApplianceType.objects.filter(appliance_class__name=appliance_class)
	
	wattage = []
	for x in types:
		wattage.append(x.wattage)
	res = {
		'wattage': wattage
	}

	return HttpResponse(json.dumps(res), content_type="application/json")

@login_required
def usage(request):
	context = RequestContext(request)
	
	user_p = UserProfile.objects.filter(user=request.user)
	usage = ApplianceUsage.objects.filter(user = user_p)

	res = []
	for x in usage:
		name = x.appliance_type.appliance_class.name
		wattage = x.appliance_type.wattage
		amount = x.amount
		res.append({'name': name, 'wattage': wattage, 'amount': amount})

	return HttpResponse(json.dumps(res), content_type="application/json")	