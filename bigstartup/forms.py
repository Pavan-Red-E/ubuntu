from django import forms
from .models import startup

class incubationForm(forms.ModelForm):
	class Meta:
		model = startup
		fields = ('name_of_enterprise',
				  'name_of_enterpreneur',
				  'email',
				  'phone_number',
				  'nationality',
				  'dob',
				  'address',
				  'education',
				  'website',
				  'organization_type',
				  'is_your_enterprise',
				  'impact',
				  'nu_mentor',
				  'name_of_mentor',
				  'sector',
				  'mention',
				  'infra_resource',
				  'special_req',
				  'pro_req',
				  'employee_space',
				  'current_space',
				  'descr',
				  'descr_bplan',
				  'attachment_of_bplan',
				  'sourc_fund',
				  'benefic',
				  'stp_benefit',
				  'if_select',
				  'other_de',
				  'Signature',

				  )