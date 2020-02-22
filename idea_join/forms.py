from django import forms
from .models import idea

class ideaForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100,widget= forms.TextInput(attrs={'class': "form-group"}))
    last_name = forms.CharField(label='Last Name', max_length=100,widget= forms.TextInput(attrs={'class': "form-group"}))
    email = forms.EmailField(widget= forms.TextInput(attrs={'class': "form-group"}))
    enrollment_no = forms.CharField(label='Enrollment Number', max_length=30,widget= forms.TextInput(attrs={'class': "form-group"}))
    why_do_you_want_to_join_CIIE  = forms.CharField(widget= forms.Textarea(attrs={'class': "form-group"}))
    join_ciie = forms.BooleanField(label='Join CIIE')
