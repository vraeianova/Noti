# Django
from django.views.generic import TemplateView,View,DeleteView
from django.http import JsonResponse
from django.urls import reverse_lazy


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


class DeleteNoteView(View):
	# model = Notes
	def post(self, request, **kwargs):
		data = json.loads(self.request.body)		
		Notes.objects.filter(pk=data['note_id']).delete()
		
		return JsonResponse({'data':"ok"}, status = 200, safe=False)

class DeleteAllNotesView(View):
	def post(self, request, **kwargs):		
		Notes.objects.all().delete()
		return JsonResponse({'data':"ok"}, status = 200, safe=False)
		
class DeleteSelectedNotesView(View):
	def post(self, request, **kwargs):	
		data = json.loads(self.request.body)		
		note_ids = data['note_ids']
		Notes.objects.filter(pk__in=note_ids).delete()

		print('borré')
		return JsonResponse({'data':"ok"}, status = 200, safe=False)


class CompleteNoteView(View):
	def post(self, request, **kwargs):
		data = json.loads(self.request.body)		
		is_completed = data['completed']
		print('verificar',is_completed)
		if is_completed:	
			Notes.objects.filter(pk=data['note_id']).update(is_completed=False)
		else:
			Notes.objects.filter(pk=data['note_id']).update(is_completed=True)
				
		return JsonResponse({'data':"ok"}, status = 200, safe=False)