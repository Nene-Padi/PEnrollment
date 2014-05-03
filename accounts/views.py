from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.formtools.wizard.views import SessionWizardView
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm


def login(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'accounts/login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user =  auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/home')
	else:
		return HttpResponseRedirect('/accounts/invalid')	

def loggedin(request):
	return render(request, 'accounts/loggedin.html', 
				{'full_name':request.user.username})

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def invalid(request):
	return render(request, 'accounts/invalid.html')

def register_user(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/registered/')

	args = {}
	args.update(csrf(request))
	
	args['form'] = RegistrationForm()

	return render(request, 'accounts/register.html', args)


def registered(request):
	return render(request, 'accounts/registered.html')