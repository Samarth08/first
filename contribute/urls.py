from . import views
from django.conf.urls import url, include
from django.conf import settings
urlpatterns =[
    url(r'^$', views.contribute , name='contribute'),
#    url(r'^thankyou/',views.thank, name='thank')    
   ]
