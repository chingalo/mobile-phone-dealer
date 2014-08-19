from django.db import models

class Dealer(models.Model):
	name = models.CharField(max_length = 200)
	e_mail = models.EmailField(max_length = 200)
	mobile_number = models.CharField(max_length = 200)
	username = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	login_status = models.CharField(max_length = 200, default = 'log_out')
	account_ status = models.CharField(max_length = 200, default = 'active')
	
	def __unicode__(self):
		return self.name
	
	

class Phone(models.Model):
	dealer = models.ForeignKey('Dealer',on_delete = models.CASCADE)
	brand_of_Phone = models.CharField(max_length = 200)
	model_of_Phone = models.CharField(max_length = 200)
	description = models.TextField(max_length = 20000, blank = True)
	quantity = models.IntegerField(max_length = 200)
	price = models.IntegerField(max_length = 200)
	status = models.CharField(max_length = 200 , default = 'new')
	
	def __unicode__(self):
		return self.model_of_Phone

class Phone_gallery(models.Model):
	brand = models.ForeignKey('Phone',on_delete = models.CASCADE)
	image = models.ImageField(upload_to='gallery')
	
	def __unicode__(self):
		return self.brand.model_of_Phone

