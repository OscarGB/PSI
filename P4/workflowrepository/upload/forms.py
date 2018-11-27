from django import forms
from data.models import Workflow, Category

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=Category.name_max_length, help_text="Please enter the category name.")
	created = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput())
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	tooltip = forms.CharField(max_length=512, help_text="Please enter a tooltip")
	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Category
		fields = ('name', 'tooltip')


class WorkflowForm(forms.ModelForm):
	name = forms.CharField(max_length=Workflow.name_max_length, help_text="Please enter the name of the workflow")
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	description = forms.CharField(max_length=Workflow.description_max_length, help_text="Please enter the description")
	views = forms.IntegerField(widget=forms.HiddenInput(), required=False)
	downloads = forms.IntegerField(widget=forms.HiddenInput(), required=False)
	versionInit = forms.CharField(max_length=Workflow.name_max_length, help_text="Please enter the version")
	category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)
	client_ip = forms.CharField(widget=forms.HiddenInput(), required=False)
	keywords = forms.CharField(max_length=Workflow.keywords_max_length, help_text="Please enter keywords")
	json = forms.FileField()
	created = forms.DateField(widget=forms.HiddenInput(), required=False)
	


	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')
		# If url is not empty and doesn't start with 'http://',
		# then prepend 'http://'.
		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url'] = url

			return cleaned_data

	class Meta:
		# Provide an association between the ModelForm and a model
		model = Workflow
		# What fields do we want to include in our form?
		# This way we don't need every field in the model present.
		# Some fields may allow NULL values, so we may not want to include them.
		# Here, we are hiding the foreign key.
		# we can either exclude the category field from the form,
		exclude = ('slug',)
		# or specify the fields to include (i.e. not include the category field)
		#fields = ('title', 'url', 'views')