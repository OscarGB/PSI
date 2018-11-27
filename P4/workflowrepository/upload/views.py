# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
import json

from data.models import Category, Workflow
from upload.forms import WorkflowForm
from find.views import workflow_detail

from django.template.defaultfilters import slugify

def workflow_download(request, id, slug, count=True):
	consulta = Workflow.objects.filter(slug=slug)
	if not consulta:
		return None
	else:
		if(count):
			consulta[0].downloads+=1
			consulta[0].save(update_fields=["downloads"])
		filename = "Workflow.json"
		response = HttpResponse(consulta[0].json, content_type="application/octet-stream")
		response['Content-Disposition'] = 'inline; filename=%s' %filename
		return response


def download_json(request, workflow_slug):
	consulta = Workflow.objects.filter(slug=workflow_slug)
	if not consulta:
		return None
	else:
		return HttpResponse(consulta[0].json, content_type="application/json")

def add_workflow(request):
	form = WorkflowForm()
	if request.method == 'POST':
		form = WorkflowForm(request.POST, request.FILES)
		if form.is_valid():
			workflowFile = request.FILES['json']
			file_data = workflowFile.read().decode('utf-8')
			form.instance.json=file_data
			form.instance.views = 0
			form.instance.downloads = 0
			form.instance.client_ip = request.META['REMOTE_ADDR']
			workflow_slug = slugify(form.instance.name)
			form.save(commit=True)


			return workflow_detail(request, 1, workflow_slug)
		else:
			print(form.errors)
	return render(request, 'upload/add_workflow.html', {'form':form})