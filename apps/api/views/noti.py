# Django
from django.views.generic import TemplateView,View
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
		
			
class GetNotesView(View):
		
	def get(self, request, **kwargs):
		orders = list(Notes.objects.filter().values(
			'pk',
			'note',
			'is_completed',
		))
		
		return JsonResponse(orders, status = 200, safe=False)


class AddNotesView(View):
			
	def post(self, request, **kwargs):
		# print('hice post',self.request.POST)
		data = json.loads(self.request.body)
		print("data de prueba",data['note'])
		# orders = list(Notes.objects.create(note=data['note'])
		Notes.objects.create(note=data['note'])
		
		return JsonResponse({'data':"ok"}, status = 200, safe=False)