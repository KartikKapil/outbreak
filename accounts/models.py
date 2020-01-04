from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.urls import reverse

userTypes = [('P', 'Patient'), ('H', 'Hospital')]

class UserManager(BaseUserManager):
	def create_user(self, user_id, user_type, password=None):
		if not user_id:
			return ValueError("Please Enter a user_id")
		if not password:
			return ValueError("Please Enter a password")
		
		user = self.model(
			user_id = user_id,
			user_type = user_type
		)
		user.set_password(password)

		user.save(using=self._db)
		return user
	
	def create_superuser(self, user_id, user_type, password=None):
		user = self.create_user(
			user_id = user_id,
			password = password,
			user_type = user_type
		)

		user.is_admin = True
		user.is_superuser = True
		user.is_staff = True

		user.save(using=self._db)
		return user

class User(AbstractBaseUser):
	user_id = 			models.CharField(max_length=100, blank=False, unique=True)
	user_type = 		models.CharField(max_length=2, choices=userTypes, default='Patient')

	# Necessary Fields for Django User Model
	date_joined = 		models.DateTimeField(verbose_name="date-joined", auto_now_add=True)
	last_login = 		models.DateTimeField(verbose_name="last-login", auto_now=True)
	is_admin = 			models.BooleanField(default=False)
	is_active =			models.BooleanField(default=True)
	is_staff = 			models.BooleanField(default=False)
	is_superuser = 		models.BooleanField(default=False)

	USERNAME_FIELD = 'user_id'
	REQUIRED_FIELDS = ['user_type']
	
	objects = UserManager()

	def __str__(self):
		return self.user_id
	
	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True


class Patient(models.Model):
	user = 				models.OneToOneField(User, on_delete = models.CASCADE)
	name =	 			models.CharField(max_length=250)
	age = 				models.IntegerField(default=None)
	Gender = 			[('Male','M'), ('Female','F'), ('Others','O'),]	#selection of gender
	gender = 			models.CharField(max_length=6, choices=Gender, default='Male')
	contact_no = 		models.IntegerField(unique=True, blank=False)
	Social_Status = 	[('SC','SC'), ('Gen','Gen'), ('ST','ST'), ('OBC','OBC'),]
	social_status = 	models.CharField(max_length=5, choices=Social_Status, default='Gen')
	prefd_hospital = 	models.CharField(max_length=100)

	def __str__(self):
		return self.name



class Hospital(models.Model):
	user = 				models.OneToOneField(User, on_delete = models.CASCADE)
	name = 				models.CharField(max_length=250)
	address = 			models.CharField(max_length=250)
	bed_capacity = 		models.CharField(max_length=250)
	currently_free = 	models.CharField(max_length=250)

	def __str__(self):
		return self.name+', '+self.address+', '+self.currently_free+', '+self.longi+', '+self.lati