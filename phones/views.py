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
	allHtc = []
	allSony = []
	for phone in allPhones:
		if phone.brand_of_Phone == 'nokia':
			allNokia.append(phone)
		elif phone.brand_of_Phone == 'htc':
			allHtc.append(phone)
		elif phone.brand_of_Phone == 'sony':
			allSony.append(phone)
	
	nokia = len(allNokia)
	htc = len(allHtc)
	sony = len(allSony)
	
	context = {'allPhones':allPhones,'allSony':allSony,'allNokia':allNokia,'allHtc':allHtc,'allImages':allImages,'nokia':nokia,'htc':htc,'sony':sony }
	return render(request,'index.html',context)

