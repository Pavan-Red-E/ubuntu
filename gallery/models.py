from django.db import models

# Create your models here.
class Image(models.Model):
	title		= models.CharField(max_length=255)
	description = models.TextField(default='insert');
	image		= models.ImageField(upload_to = "gallery", default='default.jpg', blank=True)

	def __str__(self):
		return self.title