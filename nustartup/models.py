from django.db import models

# Create your models here.
class nustartup(models.Model):
	title		= models.CharField(max_length=255)
	description = models.TextField(default='insert');
	team        =models.TextField(default='insert');
	logo		= models.ImageField(upload_to = "events",default='default.jpg', blank=True)
	url			= models.CharField(max_length=255)
	
	def __str__(self):
		return self.title