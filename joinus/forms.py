from django import forms
from .models import join

class joinForm(forms.ModelForm):
	class Meta:
		model = join
		fields = ('first_name','last_name','email','enrollment_no','why_do_you_want_to_join_CIIE')