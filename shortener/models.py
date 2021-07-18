from django.db import models

# Create your models here.
class Url(models.Model):
	short_url = models.CharField(primary_key = True, max_length=128)
	long_url = models.CharField(unique = True, max_length=2048)

	def __str__(self):
		return self.short_url + ':' + self.long_url
