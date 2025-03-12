from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserForm(UserCreationForm):

	first_name = forms.CharField(max_length = 50, required= True)
	last_name = forms.CharField(max_length = 50, required= True)
	email = forms.EmailField(max_length = 50, required= True)

	class Meta: #Tells the django that extra fields have been added other than the default formm fields
		model = User
		fields = ('username','first_name','last_name','email','password1','password2')

	def save(self, commit = True):
		user = super(UserForm, self).save(commit = False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user



