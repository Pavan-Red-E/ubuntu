from django.shortcuts import render
from .forms import joinForm
# Create your views here.
def join(request):
	template="join.html"

	if request.method == "POST":
		form = joinForm(request.POST)

		if form.is_valid():
			form.save()

	else:
		form = joinForm()

	context = {
		'form' : form 
	}			

	return render(request, template, context)