from django.db import models
from django.urls import reverse
# Create your models here.
import uuid
class Patient_name(models.Model):
	name = models.CharField(max_length=250)
	age = models.IntegerField(default=None)
	Gender = [('Male','M'),('Female','F'),('Others','O'),]#selection of gender
	gender = models.CharField(max_length=2,choices=Gender,default='Male')
	contact_no = models.IntegerField(unique=True,blank=False)
	Social_Status = [('SC','SC'),('Gen','Gen'),('ST','ST'),('OBC','OBC'),]
	social_status = models.CharField(max_length=5,choices=Social_Status,default='Gen')
	user_id = models.CharField(max_length=100,blank=False)
	pass_word = models.CharField(max_length=25,blank=False)
	Prefferd_hospital = models.CharField(max_length=100)


class Hospital_Name(models.Model):
	name = models.CharField(max_length=250)
	longi = models.CharField(max_length=250)
	lati = models.CharField(max_length=250)
	address = models.CharField(max_length=250)
	bed_capacity = models.CharField(max_length=250)
	currently_free = models.CharField(max_length=250)
	user_id = models.CharField(max_length=100, blank=False)
	pass_word = models.CharField(max_length=25, blank=False)
	def __str__(self):
		return self.name+','+self.address+','+self.currently_free+','+self.longi+','+self.lati