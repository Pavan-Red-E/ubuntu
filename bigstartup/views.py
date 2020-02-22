from django.shortcuts import render
from .forms import incubationForm
# Create your views here.
def incub(request):
	template="startup.html"

	if request.method == "POST":
		form = incubationForm(request.POST)

		if form.is_valid():
			form.save()

	else:
		form = incubationForm()

	context = {
		'form' : form ,
	}			

	return render(request, template, context)