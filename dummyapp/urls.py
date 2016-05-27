from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^first$',views.firstview,name='firstview'),
   	url(r'^second$',views.secondview,name='secondview'),
 	

    ]
