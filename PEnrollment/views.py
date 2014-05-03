from django.shortcuts import render

def intro(request):
	return render(request, 'intro.html')

def home(request):
	return render(request, 'home.html')