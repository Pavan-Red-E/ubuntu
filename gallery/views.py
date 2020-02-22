from django.shortcuts import render
from .models import Image

# Create your views here.
def gallery(request):
	pics = Image.objects.all()
	return render(request,'gallery.html',{'pics':pics})

