from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
import json 
from django.core.mail import send_mail
from random import randrange
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from phones.models import *


#home page
def home(request):
	allPhones = Phone.objects.all()
	allImages = Phone_gallery.objects.all()
	
	allNokia = []
	nokia = 0
	allHtc = []
	htc = 0
	allSony = []
	sony = 0
	for phone in allPhones:
		if phone.brand_of_Phone == 'nokia':
			allNokia.append(phone)
			nokia += phone.quantity
			
		elif phone.brand_of_Phone == 'htc':
			allHtc.append(phone)
			htc += phone.quantity
			
		elif phone.brand_of_Phone == 'sony':
			allSony.append(phone)
			sony += phone.quantity
	
	 
	
	context = {'allPhones':allPhones,'allSony':allSony,'allNokia':allNokia,'allHtc':allHtc,'allImages':allImages,'nokia':nokia,'htc':htc,'sony':sony }
	return render(request,'index.html',context)



#send contatc form to me
def sendContact(request):	
	if request.POST:
		form = request.POST
		name = form.getlist('name')
		mobilenumber = form.getlist('mobilenumber')
		email = form.getlist('email')
		rate = form.getlist('rate')
		messages = form.getlist('message')
		subject = "COMMENTS, RATING AND PROPASSAL FROM MobileTz"
		message = "Name : " + name[0] + "\nE-mail : " + email[0] + "\nMobile number : " + mobilenumber[0] + "\nMessage : " + messages[0] + "\nRating : " + str(rate[0])
		recipient_list = ['profschingalo@gmail.com']
		from_email = ""
		
		send_mail(subject,message,from_email,recipient_list,fail_silently=False)
		
	return HttpResponseRedirect('/')






#login process
def login(request):
	
	if request.POST:
				
		dealers = Dealer.objects.all()
		
		form = request.POST
		username = form.getlist('username')
		password = form.getlist('password') 
		dealerStatus = ""
		
		for dealer in dealers:
			if dealer.username == username[0] and dealer.password == password[0] :
				dealerStatus = 'member'
		if	dealerStatus == 'member':
			dealer = Dealer.objects.get(username = username[0])
			dealer.login_status = "login"
			dealer.save()
			
			return render(request, 'login.html',{'loginDealer':dealer})
		else:
			
			return render(request, 'loginTry.html',{'username':username[0]})			
					
	return HttpResponseRedirect('/#login')




#dealer home
def dealerHome(request, user_id):
	
	dealer = Dealer.objects.get(id = user_id)	
	return render(request, 'login.html',{'loginDealer':dealer})




#my store home
def myStore(request, user_id):
	
	loginDealer = Dealer.objects.get(id = user_id)
	allProducts = Phone.objects.filter(dealer = loginDealer)
	
	context = {'loginDealer': loginDealer,'allProducts':allProducts }
	return render(request, 'mystore.html',context)



#product managements home
def productManagement(request, user_id):
	
	loginDealer = Dealer.objects.get(id = user_id)
	#allProducts = Phone.objects.filter(dealer = loginDealer)
	
	context = {'loginDealer': loginDealer,}
	return render(request, 'productManagement.html',context)



#account manageents home
def accountManagement(request, user_id):
	
	loginDealer = Dealer.objects.get(id = user_id)
	#allProducts = Phone.objects.filter(dealer = loginDealer)
	
	context = {'loginDealer': loginDealer,}
	return render(request, 'accountManagement.html',context)


#log out process
def logout(request, user_id):
	
	 logoutDealer = Dealer.objects.get(id = user_id)
	 logoutDealer.login_status = "logout"
	 logoutDealer.save()
	 
	 return HttpResponseRedirect('/')
				
def logoutForm(request):
	
	return render(request, 'loginTry.html',{'username':"","password":""})
