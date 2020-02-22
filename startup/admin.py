from django.contrib import admin
from .models import startup
from django.utils.html import format_html
from django.urls import reverse
from django.conf.urls import url 
from .views import serve_pdf_preview 


# Register your models here.

@admin.register(startup)
class AccountAdmin(admin.ModelAdmin):
	date_heirarchy = (
		'modified',
	)
	list_display = (
		'name_of_enterprise',
		'name_of_enterpreneur',
		'email',
		'phone_number',
		'nationality', 
		'generate_pdf_preview_html',
	)

	readonly_fields = (
		'name_of_enterprise',
		'name_of_enterpreneur',
		'email',
		'phone_number',
		'nationality', 
	)
	 
	def generate_pdf_preview_html(self, obj):
		return format_html('<a class="button" href="%s/gen_pdf_preview/">Export as PDF</a>' % obj.id)
		
	generate_pdf_preview_html.short_description = 'Generate pdf preview'
	generate_pdf_preview_html.allow_tags = True

	def get_urls(self):
		from django.urls import path

		urls = super().get_urls()
		custom_urls = [path('<path:object_id>/gen_pdf_preview/', self.admin_site.admin_view(serve_pdf_preview),
				 name='vision_questionarioistituzionescolastica_generatepdf')
		]

		return custom_urls + urls
