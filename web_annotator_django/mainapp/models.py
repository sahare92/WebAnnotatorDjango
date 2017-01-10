from django.db import models

#User
class User(models.Model):
	email = models.CharField(max_length=100, primary_key=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	affiliation = models.CharField(max_length=100)

	def as_json(self):
		return dict(email=self.email,first_name=self.first_name,last_name=self.last_name,password= self.password,affiliation=self.affiliation)
#Image
class Image(models.Model):
	name = models.CharField(max_length=100)
	src = models.CharField(max_length=1000)

#Annotation
class Geometry(models.Model):
	x = models.FloatField()
	y = models.FloatField()
	width = models.FloatField()
	height = models.FloatField()


	def as_json(self):
		return dict(x=self.x,y=self.y,width=self.width,height=self.height)

class Shape(models.Model):
	s_type = models.CharField(max_length=20)
	geometry = models.ForeignKey(Geometry, on_delete=models.CASCADE)

	def as_json(self):
		return dict(type=self.s_type,geometry=self.geometry.as_json())

class Annotation(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ForeignKey(Image, on_delete=models.CASCADE)
	text = models.CharField(max_length = 200)	
	shapes = models.ForeignKey(Shape, on_delete=models.CASCADE)

	def as_json(self):
		return dict(image=self.image.src,text=self.text,shapes=[self.shapes.as_json()])

#Collection
class MSCollection(models.Model):
	name = models.CharField(max_length = 100)

#Manuscripts
class Manuscript(models.Model):
	name = models.CharField(max_length = 200)
	collection =  models.ForeignKey(MSCollection, on_delete=models.CASCADE)
	language = models.CharField(max_length = 100)

#Page
class Page(models.Model):
	title = models.CharField(max_length = 200)
	status = models.CharField(max_length = 50)
	manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE)