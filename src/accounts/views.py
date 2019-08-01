from django.shortcuts import render 
from django.core.urlresolvers import reverse
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (

	authenticate,
	login,
	logout

	)

def LoginView(request):
	form = LoginForm(request.POST or None)
	if request.method =="POST":
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			login(request, user)
			return HttpResponseRedirect(reverse("accounts:home"))

	context = {
		'form':form 
	}
	return render(request, 'accounts/login.html', context)

@login_required
def LogoutView(request):
	logout(request)
	return HttpResponseRedirect(reverse('accounts:login'))

@login_required
def func(request):
	return render(request,'accounts/home.html')

def contact(request):
	return render(request,'contact.html')	
