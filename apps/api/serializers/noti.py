"""Noti serializer."""
from rest_framework import serializers
from apps.api.models import Notes 


class NotesModelSerializer(serializers.ModelSerializer):
	"""Notes model serializer."""

	class Meta:
		"""Meta class."""

		model = Notes
		
		fields = (
			'note',
			'is_completed',
		)
