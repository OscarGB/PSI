from django.conf.urls import url
from data import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# url(r'^help/$', views.help, name='help'),
	# url(r'^workflow_search/$', views.workflow_search, name='workflow_search'),
	url(r'^workflow_download_json/(?P<workflow_slug>[\w\-]+)/$', views.download_json, name="download_json"),
	url(r'^workflow_list/(?P<category_slug>[\w\-]+)/$', views.workflow_list, name="workflow_list"),
	url(r'^workflow_list/$', views.index, name="index"),
	# url(r'^workflow_download/(?P<workflow_id>[\w\-]+)/(?P<workflow_slug>[\w\-]+)/$', views.workflow_download, name="workflow_download"),
	url(r'^workflow_detail/(?P<workflow_slug>[\w\-]+)/$', views.workflow_detail, name="workflow_detail"),
	
]