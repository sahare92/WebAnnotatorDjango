from django.http import HttpResponse
from models import Annotation, Shape, Geometry, User
from django.core import serializers
import json

def processRequest(request):
	if request.method == 'GET':
	    return handleGet(request)
	elif request.method == 'POST':
	    return handlePost(request)

	return handleGet(request)

def handleGet(request):
	c = Geometry(x=0.1,y=0.1,width=0.1,height=0.1)
	c.save()
	b = Shape(s_type='rect',geometry=c)
	b.save()
	a = Annotation(src='dog.jpg',text='anno1',shapes=b)
	a.save()

	res = []
	for anno in Annotation.objects.all():
		res.append(json.dumps(anno.as_json()))

	return HttpResponse(res[0], content_type="application/json")

def handlePost(request):
	request_data = json.load(request.body)
	if(isValidUser(request_data)):
		new_user = User(email=request_data["email"],first_name=request_data["first_name"],last_name=request_data["last_name"],password=request_data["password"],affiliation=request["affiliation"])
		new_user.save()
	else:
		return 'error'

	res = []
	for user in User.objects.all():
		res.append(json.dumps(user.as_json()))

	return HttpResponse(res[0], content_type="application/json")

def isValidUser(details):
	return True;