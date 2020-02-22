from django.db import models

class startup(models.Model):
	name_of_enterprise = models.CharField(max_length=50)
	name_of_enterpreneur  = models.CharField(max_length=50)
	email      = models.EmailField()
	phone_number  = models.CharField(max_length=50)
	nationality  = models.CharField(max_length=50)

	def __str__(self):
		return self.name_of_enterprise