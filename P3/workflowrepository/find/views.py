# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json

from data.models import Category, Workflow

def workflow_detail(request, id, slug):
	consulta = Workflow.objects.filter(slug=slug)
	if not consulta:
		return render(request, 'find/error.html')
	else:
		context_dict = {'workflow': consulta[0]}
		context_dict["categories"] = consulta[0].category.all()
		return render(request, 'find/workflow.html', context=context_dict)
		
def download_json(request, workflow_slug):
	consulta = Workflow.objects.filter(slug=workflow_slug)
	if not consulta:
		return None
	else:
		return HttpResponse(json.loads(consulta[0].json), content_type="application/json")

def index(request):
	workflows = Workflow.objects.all()
	categories = Category.objects.all()
	context_dict = {"workflows":workflows, "categories":categories}
	return render(request, 'find/index.html', context=context_dict)

def workflow_list(request, category_slug):
	category = Category.objects.filter(slug=category_slug)[0]
	workflows_aux = Workflow.objects.all()
	workflows = []
	for a in workflows_aux:
		for b in a.category.all():
			if b.slug == category.slug:
				workflows.append(a)

	categories = Category.objects.all()
	context_dict = {"workflows":workflows, "categories":categories, "category":category}
	return render(request, 'find/category.html', context=context_dict)

def workflow_list_by_category(request, category_slug):
	return workflow_list(request, category_slug)

def help(request):
	categories = Category.objects.all()
	context_dict = {"categories":categories}
	return render(request, 'find/help.html', context=context_dict)

def search(request):
	nombre = request.POST.get("key")
	try:
		w = Workflow.objects.filter(name=nombre)[0]
	except Exception:
		return render(request, 'find/error.html')
	return workflow_detail(request,1, w.slug)

def workflow_download(request, id, slug):
	return download_json(request, slug)