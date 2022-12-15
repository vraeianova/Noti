
from rest_framework.generics import ListAPIView
from ..serializers import NotesModelSerializer
from ..models import Notes

class NotiApiView(ListAPIView):
	serializer_class = NotesModelSerializer

	def get_queryset(self):
		return Notes.objects.all()