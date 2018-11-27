from django.conf.urls import url
from upload import views

urlpatterns = [
	url(r'^workflow_download_json/(?P<workflow_slug>[\w\-]+)/$', views.download_json, name="download_json"),
	url(r'^workflow_download/(?P<id>\d+)/(?P<slug>[\w\-]+)/$', views.workflow_download, name="workflow_download"),
	url(r'add_workflow/$', views.add_workflow, name="add_workflow"),
]
	