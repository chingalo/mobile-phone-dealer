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
			return render(request, 'login.html',{'loginDealer':dealer})
		else:
			
			return render(request, 'loginTry.html',{'username':username[0]})			
					
	return HttpResponseRedirect('/#login')
	

			
		
		
