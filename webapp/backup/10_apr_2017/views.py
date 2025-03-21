from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View

from webapp.models import Dj_Bookrelation, Dj_Book_issued
from webapp.form import UserForm
#import json as simplejson
import datetime

def index(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('webapp/login.html',c)


def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username = username, password = password)

	if user is not None:
		if user.is_active:
			auth.login(request, user)
			return redirect('/home/')
	else:
		#return render(request, 'webapp/signup.html', {'form':form})
		return redirect('/login/')


def home(request):
	# Registration page
	return render(request, 'webapp/dashboard.html')

def sign_up(request):

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			#user = form.save(commit = False)
			form.save()
			return redirect('/welcome/')
		else:
			form = UserForm()
			return render(request, 'webapp/signup.html', {'form':form})
	else:
		form = UserForm()
		return render(request, 'webapp/signup.html', {'form':form})


def welcome(request):
	# Registration success page
	return render(request, 'webapp/welcome.html')


def search(request):
	book_data =  list(Dj_Bookrelation.objects.all())
	return render(request, 'webapp/searchabook.html',{'book_data':book_data})

def issueabook(request):
	book_data =  list(Dj_Bookrelation.objects.all())
	#return render(request, 'webapp/searchabook.html',{'book_data':book_data})
	return render(request, 'webapp/issueabook.html',{'book_data':book_data})

def logout(request):
	auth.logout(request)
	return render(request,'webapp/logout.html')


def checkbox_auth(request):
	book_data =  list(Dj_Bookrelation.objects.all())
	if request.method == "POST":
		display_type = request.POST.get("display_type", None)
		for bookvar in book_data:
			#print(bookvar.Dj_Book_isbn)
			if display_type in [bookvar.Dj_Book_isbn]:
				#print(display_type)
				#user_id = User.objects.get(username=request.user.username).pk
				user_id = request.user
				#book_isbn = bookvar.Dj_Book_isbn
				book_isbn = Dj_Bookrelation.objects.get(Dj_Book_isbn=bookvar.Dj_Book_isbn)
				book_name = bookvar.Dj_Book_name
				issued_on = datetime.date.today()
				due_date = datetime.date.today() + datetime.timedelta(1*365/12)
				print(user_id,book_isbn,book_name,issued_on,due_date)

				insert_data = Dj_Book_issued(Dj_user= user_id, Dj_Book_isbn= book_isbn, Dj_Book= book_name, Dj_issued_on= issued_on, Dj_due_date= due_date)
				insert_data.save()


	return render(request, 'webapp/issueabook.html', {'book_data': book_data})
