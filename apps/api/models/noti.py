"""Notes model."""

# Django
from django.db import models
from django.conf import settings
from apps.utils.directory_path import user_profile_pic_directory_path
from django.contrib import admin

class Notes(models.Model):
	""" Notes model.
		This model holds notes data.
	"""
	id = models.AutoField(db_column='IdNote', primary_key=True)
	note = models.CharField(db_column='Note', max_length=255, blank=True, null=True)
	is_completed = models.BooleanField(db_column='IsCompleted', default=True)
	
	def __str__(self):
		"""Return Notes."""
		return str(self.note)


admin.site.register(Notes)
