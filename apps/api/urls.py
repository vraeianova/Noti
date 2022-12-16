"""Api URLs."""

# Django
from django.urls import include, path

# Django REST Framework
# from rest_framework.routers import DefaultRouter

# Views
from .views import (NotiApiView,NotiView,GetNotesView,AddNotesView,DeleteNoteView)

# router = DefaultRouter()
# router.register(r'users', user_views.UserViewSet, basename='users')

urlpatterns = [
	# path('', include(router.urls))
	path('',NotiView.as_view(),name="notes"),

	path('api/noti/list',NotiApiView.as_view(),name="noti_list"),
	path('api/noti/get/',GetNotesView.as_view(),name="get_notes"),
	path('api/noti/post/',AddNotesView.as_view(),name="post_note"),
	path('api/noti/<pk>/delete/',DeleteNoteView.as_view(),name="delete_note"),

]
