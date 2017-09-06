from django.conf.urls import url, include
from django.views.generic import ListView,DetailView
from django.conf import settings
from contribute.models import SignUp
urlpatterns = [
    url(r'^$',ListView.as_view(queryset=SignUp.objects.all().order_by("-timestamp")[:25],template_name="Article/Articles.html")),
    url(r'^(?P<pk>\d+)$',DetailView.as_view(model=SignUp,template_name ='Article/art.html'))]

#,'django.views.static.serve',{'document_root': settings.MEDIA_ROOT,}
