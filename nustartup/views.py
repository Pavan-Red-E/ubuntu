from django.shortcuts import render
from .models import nustartup


# Create your views here.
def startups(request):
	startups=nustartup.objects.all
	return render(request,'startup/startups.html',{'startups':startups})


def startup(request):
	id=request.GET.get('id', '')	#Get attribute from url
	startup=nustartup.objects.get(pk=id)	#get model from database by id
	return render(request,'startup/startupPage.html',{'startup':startup}) #send model to view renderer 


