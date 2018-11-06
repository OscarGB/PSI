# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json

from data.models import Category, Workflow
# from data.forms import CategoryForm, PageForm

def workflow_detail(request, workflow_slug):
	consulta = Workflow.objects.filter(slug=workflow_slug)
	if not consulta:
		return render(request, 'data/error.html')
	else:
		context_dict = {'workflow': consulta[0]}
		context_dict["categories"] = consulta[0].category.all()
		return render(request, 'data/workflow.html', context=context_dict)
		
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
	return render(request, 'data/index.html', context=context_dict)

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
	return render(request, 'data/category.html', context=context_dict)


# def index(request):
# 	# Construct a dictionary to pass to the template engine as its context.
# 	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
# 	category_list = Category.objects.order_by('-likes')[:5]
# 	pages_list = Page.objects.order_by('-views')[:5]
# 	context_dict = {"categories": category_list, "pages": pages_list}
# 	# context_dict = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupcake!"}

# 	# Return a rendered response to send to the client.
# 	# We make use of the shortcut function to make our live easier.
# 	# Note that the first parameter os the template we wish to use.
# 	return render(request, 'rango/index.html', context=context_dict)
# 	# return HttpResponse("<p>Rango says hey there partner!</p><a href='/rango/about/'>About page</a>")

# def show_category(request, category_name_slug):
# 	# Create a context dictionary which we can pass
# 	# to the template rendering engine.
# 	context_dict = {}
# 	try:
# 		# Can we find a category name slug with the given name?
# 		# If we can't, the .get() method raises a DoesNotExist exception.
# 		# So the .get() method returns one model instance or raises an exception.
# 		category = Category.objects.get(slug=category_name_slug)

# 		# Retrieve all of the associated pages.
# 		# Note that filter() will return a list of page objects or an empty list
# 		pages = Page.objects.filter(category=category)

# 		# Adds our results list to the template context under name pages.
# 		context_dict['pages'] = pages

# 		# We also add the category object from
# 		# the database to the context dictionary.
# 		# We'll use this in the template to verify that the category exists.
# 		context_dict['category'] = category

# 	except Category.DoesNotExist:
# 		# We get here if we didn't find the specified category.
# 		# Don't do anything -
# 		# the template will display the "no category" message for us.
# 		context_dict['category'] = None
# 		context_dict['pages'] = None

# 	# Go render the response and return it to the client.
# 	return render(request, 'rango/category.html', context_dict)

# def about(request):
# 	return render(request, 'rango/about.html')

# def add_category(request):
# 	form = CategoryForm()
# 	# A HTTP POST?
# 	if request.method == 'POST':
# 		form = CategoryForm(request.POST)
# 		# Have we been provided with a valid form?
# 		if form.is_valid():
# 			# Save the new category to the database.
# 			form.save(commit=True)
# 			# Now that the category is saved
# 			# We could give a confirmation message
# 			# But since the most recent category added is on the index page
# 			# Then we can direct the user back to the index page.
# 			return index(request)
# 		else:
# 			# The supplied form contained errors -
# 			# just print them to the terminal.
# 			print(form.errors)
# 	# Will handle the bad form, new form, or no form supplied cases.
# 	# Render the form with error messages (if any).
# 	return render(request, 'rango/add_category.html', {'form': form})

# def add_page(request, category_name_slug):
# 	try:
# 		category = Category.objects.get(slug=category_name_slug)
# 	except Category.DoesNotExist:
# 		category = None
# 	form = PageForm()
# 	if request.method == 'POST':
# 		form = PageForm(request.POST)
# 		if form.is_valid():
# 			if category:
# 				page = form.save(commit=False)
# 				page.category = category
# 				page.views = 0
# 				page.save()
# 				return show_category(request, category_name_slug)
# 		else:
# 			print(form.errors)

# 	context_dict = {'form':form, 'category': category}
# 	return render(request, 'rango/add_page.html', context_dict)