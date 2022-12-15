"""User's models."""


# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from ..managers import CustomUserManager


class CustomUser(AbstractUser,):
	"""User model.
	Extend from Django's Abstract User, change the username field
	to email and add some extra fields.
	"""
	username = None
	first_name = models.CharField("first name", max_length=150, blank=True)
	last_name = models.CharField("last name", max_length=150, blank=True)
	
	email = models.EmailField(
		'email address',
		unique=True,
		error_messages={
			'unique': 'A user with that email already exists.'
		}
	)   
	email_confirmed = models.BooleanField(
		'verified',
		default=False,
		help_text='Set to true when the user have verified its email address.'
	)

	is_premium = models.BooleanField(db_column='IsPremium',default=False)
	is_teams = models.BooleanField(db_column='IsTeams',default=False)
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name','last_name']
	
	objects = CustomUserManager()
	
	def __str__(self):
		"""Return username."""
		return self.email

