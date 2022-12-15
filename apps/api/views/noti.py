# Django
from django.views.generic import TemplateView
from django.http import JsonResponse

# Third party
from rest_framework.generics import ListAPIView

#Models
from ..models import Notes

#Locals
from ..serializers import NotesModelSerializer
import json

class NotiApiView(ListAPIView):
	serializer_class = NotesModelSerializer

	def get_queryset(self):
		return Notes.objects.all()


class NotiView(TemplateView):
	template_name = 'api/base.html'
		
			
