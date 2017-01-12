from django.http import HttpResponse
import json

import controller

def index(request):
	return HttpResponse(controller.processRequest(request))

def registerUser(request):
	return controller.handleUserRegistration(request)

def loginUser(request):
	return controller.handleUserLogin(request)

def addCollection(request):
	return controller.handleAddCollection(request)

def addManuscript(request):
	return controller.handleAddManuscript(request)

def addPage(request):
	return controller.handleAddPage(request)

def getPageInfoAndAnnotations(request):
	return controller.handleGetPageInfoAndAnnotations(request);
