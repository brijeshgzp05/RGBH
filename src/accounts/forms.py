from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import (

	authenticate,
	login,
	logout

	)

class LoginForm(forms.Form):
	username = forms.CharField(label="", widget=forms.TextInput(attrs={'autocomplete':'off','autofocus':'on','class':'form-control', 'placeholder':'Username'}))
	password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'autocomplete':'off','class':'form-control', 'placeholder':'Password'}))

	def clean_username(self):
		username = self.cleaned_data.get("username")
		if len(User.objects.filter(username=username))==0:
			raise forms.ValidationError("Username does not exist")

		return username

	def clean_password(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		if user is None:
			raise forms.ValidationError("Wrong Username or Password")
		return password