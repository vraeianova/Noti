"""Api URLs."""

# Django
from django.urls import include, path

# Django REST Framework
# from rest_framework.routers import DefaultRouter

# Views
from .views import (
	NotiApiView,
	NotiView,
	GetNotesView,
	AddNotesView,
	DeleteNoteView,
	CompleteNoteView,
	DeleteAllNotesView,
    DeleteSelectedNotesView
)

# router = DefaultRouter()
# router.register(r'users', user_views.UserViewSet, basename='users')

urlpatterns = [
	# path('', include(router.urls))
	path('',NotiView.as_view(),name="notes"),

	path('api/noti/list',NotiApiView.as_view(),name="noti_list"),
	path('api/noti/get/',GetNotesView.as_view(),name="get_notes"),
	path('api/noti/add/',AddNotesView.as_view(),name="add_note"),
	path('api/noti/<pk>/delete/',DeleteNoteView.as_view(),name="delete_note"),
	path('api/noti/all/del/',DeleteAllNotesView.as_view(),name="delete_all_notes"),
	path('api/noti/selected/del/',DeleteSelectedNotesView.as_view(),name="delete_selected_notes"),
	path('api/noti/<pk>/complete/',CompleteNoteView.as_view(),name="complete_note"),

]
