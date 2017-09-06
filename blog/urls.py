from django.conf.urls import url, include
from . import views


urlpatterns =[
    url(r'^$', views.up , name='up'),
    url(r'^Workouts/', views.down, name='down'),
    url(r'^chest/',views.chest,name='chest'),
    url(r'^biceps/',views.chk,name='chk'), 
    url(r'^abs/',views.abs,name='abs'),
    url(r'^triceps/',views.triceps,name='triceps'),
    url(r'^back/',views.back,name='back'),
    url(r'^shoulder/',views.shoulder,name='shoulder'),
    url(r'^legs/',views.legs,name='legs'),
     ]


