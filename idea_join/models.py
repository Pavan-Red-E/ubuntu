from django.db import models

class idea(models.Model):
	first_name = models.CharField(max_length=50)
	last_name  = models.CharField(max_length=50)
	email      = models.EmailField()
	enrollment_no = models.CharField(max_length=30)
	why_do_you_want_to_join_CIIE   = models.TextField(null = True)
	join_ciie = models.BooleanField(default=True )

	def __str__(self):
		return self.first_name+' '+self.last_name