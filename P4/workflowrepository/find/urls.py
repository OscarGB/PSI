from django.conf.urls import url
from find import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^workflow_list/$', views.index, name="index"),
	url(r'^workflow_list/((?P<category_slug>[\w\-]+)/)?$', views.workflow_list, name="workflow_list"),
	url(r'^workflow_list_by_category/(?P<category_slug>[\w\-]+)/$', views.workflow_list_by_category, name="workflow_list_by_category"),
	url(r'^help/$', views.help, name="help"),
	url(r'^workflow_search/$', views.search, name="workflow_search"),
	url(r'^workflow_detail/(?P<id>\d+)/(?P<slug>[\w\-]+)/$', views.workflow_detail, name="workflow_detail"),
	
]
	