from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


# Create your views here.

def signup(request) :

	if request.method == 'POST' :
		if request.POST['password'] == request.POST['password2'] :
			try :
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html', {'error' : "Username already exists! Try Again."})

			except User.DoesNotExist :
				user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
				login(request, user)
				return render(request, 'accounts/signup.html')

		else :
			return render(request, 'accounts/signup.html', {'error' : "Passwords didn't match! Try Again."})

	else :
		return render(request, 'accounts/signup.html')


def loginview(request) :
	if request.method == 'POST' :

		try :

			user = User.objects.get(username=request.POST['username'])

			user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

			if user is not None:
				login(request, user)
				return render(request, 'accounts/login.html', {'error' : "Logged In!"})

			else :
				return render(request, 'accounts/login.html', {'error' : "Username and Password didn't match! Try Again."})

		except User.DoesNotExist :
			return render(request, 'accounts/signupagain.html')
		
	else :
		return render(request, 'accounts/login.html')
