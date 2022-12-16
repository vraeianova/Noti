from .base import *


DEBUG = True

# =================SECURITY=================
ALLOWED_HOSTS = [
	"localhost",
	"0.0.0.0",
	"127.0.0.1",
	"noti-xce2.onrender.com"
]

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': 'Noti',
	}
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'
ROOT_URLCONF = 'conf.urls'
