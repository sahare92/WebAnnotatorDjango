# -*- coding: utf-8 -*-
from django.http import HttpResponse
from models import Annotation, Shape, Geometry, User, MSCollection, Manuscript, Page
from django.core import serializers
from django.template import Context, loader
from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
from django.conf import settings
import json

#------------FOR TESTS ONLY----------------#
def handleGet(request):
	# request_body = json.loads(request.body)	
	# try:
	#  	used_collection = MSCollection.objects.get(name = request_body["collection"])
	# except MSCollection.DoesNotExist:
	#  	return HttpResponse("FAIL")	
	# try:
	#  	used_ms = Manuscript.objects.get(name = request_body["manuscript"], collection=used_collection)
	# except Manuscript.DoesNotExist:
	#  	return HttpResponse("FAIL")
	# try:
	#  	used_user = User.objects.get(email = request_body["user_email"])
	# except User.DoesNotExist:
	#  	return HttpResponse("FAIL")
	# try:
	#  	used_page = Page.objects.get(title = request_body["page_title"], manuscript=used_ms)
	# except Page.DoesNotExist:
	#  	return HttpResponse("FAIL")		 
	# relevant_annos = Annotation.objects.filter(user = used_user, page=used_page)	

	# res = []
	# for anno in relevant_annos:
	# 	res.append(anno.as_json())
	# items = {"items": res}
	# return HttpResponse(json.dumps(items), content_type="application/json")
	request
#-------------DONE TESTING-------------------#

#-------------Functions------------------#
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
		relevant_collection = MSCollection.objects.get(name=request_body["collection"]) 
	except MSCollection.DoesNotExist:
		return HttpResponse("The collection you entered doesn't exist!")	
	
	try:
		relevant_ms = Manuscript.objects.get(name=request_body["manuscript"]) 
	except Manuscript.DoesNotExist:
		return HttpResponse("The manuscript you entered doesn't exist!")	

	new_manuscript = Page(title= request_body["title"], manuscript=relevant_ms, status="untagged" , image_src=request_body["image_src"])
	new_manuscript.save()

	return HttpResponse("Added the page successfuly!")	

def handleAddAnnotation(request):
	request_body = json.loads(request.body)
	try:
		relevant_user = User.objects.get(email=request_body["user"])
	except User.DoesNotExist:
		return HttpResponse({"status":"FAIL", "value":"The User doesn't exist!"})
	try:
		relevant_page = Page.objects.get(id=request_body["page_id"])
	except Page.DoesNotExist:
		return HttpResponse({"status":"FAIL", "value": "The Page doesn't exist!"})		
	new_geometry = Geometry(x=request_body["shape"]["x"],y=request_body["shape"]["y"],width=request_body["shape"]["width"],height=request_body["shape"]["height"])
	new_geometry.save()
	new_shape = Shape(s_type=request_body["shape"]["type"], geometry=new_geometry)
	new_shape.save()
	new_anno = Annotation(user=relevant_user,page=relevant_page,text=request_body["text"],shapes=new_shape);
	new_anno.save()
	return HttpResponse({"status":"SUCCESS","value":json.dumps(new_anno.as_json())})

def handleRemoveAnnotation(request):
	request_body = json.loads(request.body)
	try:
		relevant_user = User.objects.get(email=request_body["user"])
	except User.DoesNotExist:
		return HttpResponse({"status":"FAIL", "value":"The User doesn't exist!"})
	try:
		relevant_page = Page.objects.get(id=request_body["page_id"])
	except Page.DoesNotExist:
		return HttpResponse({"status":"FAIL", "value": "The Page doesn't exist!"})	
	try: 	
		new_geometry = Geometry.objects.get(x=request_body["shape"]["x"],y=request_body["shape"]["y"],width=request_body["shape"]["width"],height=request_body["shape"]["height"])
	except Geometry.DoesNotExist:
		return HttpResponse({"status":"FAIL", "value": "The Geometry doesn't exist!"})	
	try:
		new_shape = Shape.objects.get(s_type=request_body["shape"]["type"], geometry=new_geometry)
	except Shape.DoesNotExist:
		return HttpResponse({"status":"FAIL", "value": "The Shape doesn't exist!"})	
	try:
		anno_to_remove = Annotation.objects.get(user=relevant_user,page=relevant_page,text=request_body["text"],shapes=new_shape);
	except Annotation.DoesNotExist:
		return HttpResponse({"status":"FAIL", "value": "The Annotation doesn't exist!"})	
	anno_to_remove.delete()

	return HttpResponse({"status":"SUCCESS","value":json.dumps(anno_to_remove.as_json())})

def handleUpdateAnnotation(request):
	request_body = json.loads(request.body)
	try:
		relevant_user = User.objects.get(email=request_body["user"])
	except User.DoesNotExist:
		return HttpResponse({"status":"FAIL", "value":"The User doesn't exist!"})
	try:
		relevant_page = Page.objects.get(id=request_body["page_id"])
	except Page.DoesNotExist:
		return HttpResponse({"status":"FAIL", "value": "The Page doesn't exist!"})	
	try: 	
		new_geometry = Geometry.objects.get(x=request_body["shape"]["x"],y=request_body["shape"]["y"],width=request_body["shape"]["width"],height=request_body["shape"]["height"])
	except Geometry.DoesNotExist:
		return HttpResponse({"status":"FAIL", "value": "The Geometry doesn't exist!"})	
	try:
		new_shape = Shape.objects.get(s_type=request_body["shape"]["type"], geometry=new_geometry)
	except Shape.DoesNotExist:
		return HttpResponse({"status":"FAIL", "value": "The Shape doesn't exist!"})	
	try:
		anno_to_update = Annotation.objects.get(user=relevant_user,page=relevant_page,shapes=new_shape);
	except Annotation.DoesNotExist:
		return HttpResponse({"status":"FAIL", "value": "The Annotation doesn't exist!"})	
	anno_to_update.text = request_body["text"]
	anno_to_update.save()

	return HttpResponse({"status":"SUCCESS","value":json.dumps(anno_to_update.as_json())})


#Called when starting to work on a new annotation session on a certain page
def handleGetPageInfoAndAnnotations(request):
	request_body = json.loads(request.body)	
	try:
	 	used_collection = MSCollection.objects.get(name = request_body["collection"])
	except MSCollection.DoesNotExist:
		items = {"value": "Collection doesn't exist!", "status": "FAIL"}		
		return HttpResponse(json.dumps(items), content_type="application/json")	

	try:
	 	used_ms = Manuscript.objects.get(name = request_body["manuscript"], collection=used_collection)
	except Manuscript.DoesNotExist:
		items = {"value": "Manuscript doesn't exist!", "status": "FAIL"}		
		return HttpResponse(json.dumps(items), content_type="application/json")	

	try:
	 	used_user = User.objects.get(email = request_body["user_email"])
	except User.DoesNotExist:
		items = {"value": "User doesn't exist!", "status": "FAIL"}		
		return HttpResponse(json.dumps(items), content_type="application/json")	

	try:
	 	used_page = Page.objects.get(title = request_body["page_title"], manuscript=used_ms)
	except Page.DoesNotExist:
		items = {"value": "Page doesn't exist!", "status": "FAIL"}		
		return HttpResponse(json.dumps(items), content_type="application/json")		

	relevant_annos = Annotation.objects.filter(user = used_user, page=used_page)	

	res = []
	for anno in relevant_annos:
		res.append(anno.as_json())
	items = {"value": res, "status": "SUCCESS"}
	return HttpResponse(json.dumps(items), content_type="application/json")

# Returns a HTML page and places the request's info in it
def handleGetAnnotationHTML(request):
	try:
	 	used_collection = MSCollection.objects.get(name = request.GET.get("collection"))
	except MSCollection.DoesNotExist:
		items = {"value": "Collection doesn't exist!", "status": "FAIL"}		
		return HttpResponse(json.dumps(items), content_type="application/json")	

	try:
	 	used_ms = Manuscript.objects.get(name = request.GET.get("manuscript"), collection=used_collection)
	except Manuscript.DoesNotExist:
		items = {"value": "Manuscript doesn't exist!", "status": "FAIL"}		
		return HttpResponse(json.dumps(items), content_type="application/json")	

	try:
	 	used_user = User.objects.get(email = request.GET.get("user"))
	except User.DoesNotExist:
		items = {"value": "User doesn't exist!", "status": "FAIL"}		
		return HttpResponse(json.dumps(items), content_type="application/json")	

	try:
	 	used_page = Page.objects.get(title = request.GET.get("page"), manuscript=used_ms)
	except Page.DoesNotExist:
		items = {"value": "Page doesn't exist!", "status": "FAIL"}		
		return HttpResponse(json.dumps(items), content_type="application/json")		

	relevant_annos = Annotation.objects.filter(user = used_user, page=used_page)	


	res = []
	for anno in relevant_annos:
		res.append(anno.as_json())
	items = {"value": json.dumps(res),"server_address":"http://127.0.0.1:8000/","user":used_user.email,"page_id":used_page.id,"img_src":used_page.image_src}
	template = loader.get_template("AnnotatorHTML/annotator_index.html")
	return HttpResponse(template.render(items))

# TODO: make it actually work
def handleAddFiles(request):
	fs = FileSystemStorage()
	print("entered")	
	for newfile in request.FILES:
		print("newfile added\n" + newfile.name)	
		fs.save(newfile.name, newfile)