from django.http import HttpResponse
import json

import controller

def index(request):
	return controller.handleGet(request)

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

def addAnnotation(request):
	return controller.handleAddAnnotation(request)

def removeAnnotation(request):
	return controller.handleRemoveAnnotation(request)	

def getPageInfoAndAnnotations(request):
	return controller.handleGetPageInfoAndAnnotations(request)

def getAnnotationHTML(request):
	return controller.handleGetAnnotationHTML(request)

def addFiles(request):
	return controller.handleAddFiles(request)	
