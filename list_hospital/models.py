from django.db import models
from django.urls import reverse
# Create your models here.
class Hospital_Name(models.Model):
	name=models.CharField(max_length=250)
	longi=models.CharField(max_length=250)
	lati=models.CharField(max_length=250)
	address=models.CharField(max_length=250)
	bed_capacity=models.CharField(max_length=250)
	currently_free=models.CharField(max_length=250)
	def __str__(self):
		return self.name+','+self.address+','+self.currently_free+','+self.longi+','+self.lati