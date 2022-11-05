from django.urls import path
# from .views import SignUp
from .views import index


urlpatterns = [
	path('index.html', index, name='index'),
]