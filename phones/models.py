from django.db import models

class Phone(models.Model):
	brand_of_Phone = models.CharField(max_length = 200)
	model_of_Phone = models.CharField(max_length = 200)
	description = models.TextField(max_length = 20000)
	quantity = models.IntegerField(max_length = 200)
	price = models.IntegerField(max_length = 200)
	status = models.CharField(max_length = 200 , default = 'new')
	
	def __unicode__(self):
		return self.model_of_Phone

class Phone_gallery(models.Model):
	brand = models.ForeignKey('Phone',on_delete = models.CASCADE)
	image = models.ImageField(upload_to='gallery')
	
	def __unicode__(self):
		return self.name_of_image

