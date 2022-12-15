"""Api URLs."""

# Django
from django.urls import include, path

# Django REST Framework
# from rest_framework.routers import DefaultRouter

# Views
from .views import (NotiApiView,NotiView)

# router = DefaultRouter()
# router.register(r'users', user_views.UserViewSet, basename='users')

urlpatterns = [
	# path('', include(router.urls))
    path('',NotiView.as_view(),name="notes"),

	path('api/noti/list',NotiApiView.as_view(),name="noti_list")
]
