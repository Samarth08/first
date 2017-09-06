from django.conf.urls import url, include
from django.views.generic import ListView,DetailView
from article.models import art
from django.conf import settings

urlpatterns = [
   url(r'^$',ListView.as_view(queryset=art.objects.all().order_by("-date")[:25],template_name="Article/Articles.html")),
   url(r'^(?P<pk>\d+)$', DetailView.as_view(model = art,template_name= 'Article/art.html')),
 
    ]
#,'django.views.static.serve',{'document_root': settings.MEDIA_ROOT,}
