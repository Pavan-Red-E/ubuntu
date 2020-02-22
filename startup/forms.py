from django import forms
from .models import startup

class incubationForm(forms.ModelForm):
	class Meta:
		model = startup
		fields = ('name_of_enterprise','name_of_enterpreneur','email','phone_number','nationality')