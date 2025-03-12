from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
	#/
	url(r'^login/$', views.index, name='index'),

	url(r'^logout/$', views.logout, name='logout'),

	url(r'^auth/$', views.auth_view, name='auth_view'),
	#/signup
	url(r'^sign_up/$', views.sign_up, name='sign_up'), #register
	#/home
	url(r'^home/$', views.home, name='home'),

	url(r'^welcome/$', views.welcome, name='welcome'), #register_success

	url(r'^search/$', views.search, name='search'), # search a book

	url(r'^issue/$', views.checkbox_auth, name='issueabook'),
	
	url(r'^issuedbooks/$', views.issueabook, name='issuedbook'),
	
	url(r'^return/$', views.returnbook, name='returnbook'),
	
	url(r'^editprofile/$', views.edit_profile, name='edit_profile'),
	
]