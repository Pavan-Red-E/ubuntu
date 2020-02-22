from django.shortcuts import render
from .forms import ideaForm
# Create your views here.
def idea(request):
	template="idea.html"

	if request.method == "POST":
		form = mixForm(request.POST)

		if form.is_valid():
			form.save()

	else:
		form = ideaForm()

	context = {
		'form' : form ,
	}			

	return render(request, template, context)