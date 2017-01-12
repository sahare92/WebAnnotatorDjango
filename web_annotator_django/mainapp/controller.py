from django.http import HttpResponse
from models import Annotation, Shape, Geometry, User, MSCollection, Manuscript, Page
from django.core import serializers
import json

def processRequest(request):
	if request.method == 'GET':
	    return handleGet(request)
	elif request.method == 'POST':
	    return handlePost(request)

	return handleGet(request)

def handleGet(request):
	new_geometry = Geometry.objects.create(x= 0.1, y=0.2, width=0.1, height=0.1)
	new_shape = Shape.objects.create(s_type = "rect", geometry=new_geometry)
	used_user = User.objects.get(email = "a")
	used_page = Page.objects.get(id=1)
	new_anno = Annotation.objects.create(user=used_user,page=used_page,text="Woohoo!",shapes=new_shape)

	res = json.dumps(Annotation.objects.get(text="Woohoo!"))
	return HttpResponse(res, content_type="application/json")

def handleUserRegistration(request):
	request_body = json.loads(request.body)
	new_user = User(email= request_body["email"],first_name= request_body["first_name"],last_name= request_body["last_name"],password= request_body["password"],affiliation= request_body["affiliation"])	
	new_user.save()

	return HttpResponse(request.body)

def isValidUser(details):
	return True

def handleUserLogin(request):
	request_body = json.loads(request.body)	
	try:
		res = json.dumps(User.objects.get(email=request_body["email"],password=request_body["password"]).as_json())
	except User.DoesNotExist:
		res = None	
	if res != None:
		res = request_body["email"]
	return HttpResponse(res, content_type="application/json")


#Adding Collection/MS/Page
def handleAddCollection(request):
	request_body = json.loads(request.body)
	new_collection = MSCollection(name= request_body["name"])
	new_collection.save()

	return HttpResponse("Added the collection successfuly!")

def handleAddManuscript(request):
	request_body = json.loads(request.body)
	try:
		relevant_collection = MSCollection.objects.get(name=request_body["collection"]) 
	except MSCollection.DoesNotExist:
		return HttpResponse("The collection you entered doesn't exist!")	
	new_manuscript = Manuscript(name= request_body["name"], collection=relevant_collection, language=request_body["language"])
	new_manuscript.save()

	return HttpResponse("Added the manuscript successfuly!")

def handleAddPage(request):
	request_body = json.loads(request.body)
	try:
		relevant_ms = Manuscript.objects.get(name=request_body["manuscript"]) 
	except Manuscript.DoesNotExist:
		return HttpResponse("The manuscript you entered doesn't exist!")	

	new_manuscript = Page(title= request_body["title"], manuscript=relevant_ms, status="untagged" , image_src=request_body["image_src"])
	new_manuscript.save()

	return HttpResponse("Added the page successfuly!")	

#Called when starting to work on a new annotation session on a certain page
def handleGetPageInfoAndAnnotations(request):
	request_body = json.loads(request.body)
	try:
		relevant_collection = MSCollection.objects.get(name=request_body["collection"]) 
	except MSCollection.DoesNotExist:
		return HttpResponse("The collection you entered doesn't exist!")
	try:		
		relevant_ms = Manuscript.objects.get(name=request_body["manuscript"], MSCollection=relevant_collection)
	except Manuscript.DoesNotExist:
		return HttpResponse("The manuscript you entered doesn't exist!")
	try:		
		relevant_page = Page.objects.get(title=request_body["title"], Manuscript=relevant_ms)
	except Page.DoesNotExist:
		return HttpResponse("The page you entered doesn't exist!")		
	
	output_dict = json.dumps(Annotation.objects.get(page = relevant_page).as_json())

	return HttpResponse(output_dict, content_type="application/json")
	