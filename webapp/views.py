from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View

from webapp.models import Dj_Bookrelation, Dj_Book_issued
from webapp.form import UserForm, EditProfileForm
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
	issue_book_data = list(Dj_Book_issued.objects.all())
	return render(request, 'webapp/issueabook.html',{'issue_book_data':issue_book_data})

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
				#print(user_id,book_isbn,book_name,issued_on,due_date)

				insert_data = Dj_Book_issued(Dj_user= user_id, Dj_Book_isbn= book_isbn, Dj_Book= book_name, Dj_issued_on= issued_on, Dj_due_date= due_date)
				insert_data.save()
				
				del_var_isbn = bookvar.Dj_Book_isbn
				update_bool = Dj_Bookrelation.objects.get(pk = del_var_isbn)
				update_bool.Dj_is_issued = True
				update_bool.save()
				
				#Dj_Bookrelation.objects.filter(pk=del_var).delete()
				
				
	return render(request, 'webapp/issue_success.html', {'book_data': book_data})

def returnbook(request):
	issue_book_data = list(Dj_Book_issued.objects.all())
	if request.method == "POST":
		display_type_issue = request.POST.get("display_type_issue", None)
		for issue_a_book in issue_book_data:
			#print(issue_a_book.Dj_Book_isbn_id)
			if display_type_issue in [issue_a_book.Dj_Book_isbn_id]:
				#print(display_type_issue)
				
				delete_the_book_var_bid = issue_a_book.Dj_Book_isbn_id
				delete_the_book_var_uid = issue_a_book.Dj_user_id

				Dj_Book_issued.objects.filter(pk=delete_the_book_var_bid).delete()
				
				update_bool_issued = Dj_Bookrelation.objects.get(pk = delete_the_book_var_bid)
				update_bool_issued.Dj_is_issued = False
				update_bool_issued.save()
				

	return render(request, 'webapp/return_success.html', {'issue_book_data': issue_book_data})
	
	
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance = request.user)
		
		if form.is_valid():
			form.save()
			return redirect('/home/')
		else:
			form = EditProfileForm(instance = request.user)
			return render(request,'webapp/editprofile.html', {'form':form})
	else:
		form = EditProfileForm(instance = request.user)
		return render(request,'webapp/editprofile.html', {'form':form})












