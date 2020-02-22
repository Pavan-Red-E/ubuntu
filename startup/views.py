from django.shortcuts import render
from .forms import incubationForm
from .models import startup
from NUciie.utils import render_to_pdf 
from django.template.loader import get_template
from django.http import HttpResponse

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

def serve_pdf_preview(request, object_id):
	obj=startup.objects.get(pk=object_id)

	template = get_template('pdf.html')
	html = template.render({'obj':obj})

	pdf = render_to_pdf('pdf.html',{'obj':obj})
	if pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		filename = obj.name_of_enterprise+".pdf"
		content = "inline; filename=%s" %(filename)
		download = request.GET.get("download")
		if download:
			content = "attachment; filename=%s" %(filename)
		response['Content-Disposition'] = content
		return response
	return HttpResponse("Not found")
