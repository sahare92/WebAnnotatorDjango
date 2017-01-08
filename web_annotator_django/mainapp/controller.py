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
	res = []
	res.append(json.dumps(User.objects.get(first_name="sahar1").as_json()))

	return HttpResponse(res[0], content_type="application/json")

def handleUserRegistration(request):
	request_body = json.loads(request.body)
	new_user = User(email= request_body["email"],first_name= request_body["first_name"],last_name= request_body["last_name"],password= request_body["password"],affiliation= request_body["affiliation"])	
	new_user.save()

	return HttpResponse(request.method)

def isValidUser(details):
	return True