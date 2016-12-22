from django.http import HttpResponse
import json

import controller


''' 
#request convention: (json-object)
	Get:
	type:= 'login',
	
	Post:
	type:= 'register'
	data:= The needed data for the action 
'''
def index(request):
	return HttpResponse(controller.processRequest(request))
