from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.views import logout
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/', views.login, name='login'),
	url(r'^profile/', login_required(views.profile) , name='profile'),
	url(r'^projects/', login_required(views.projects) , name='projects'),
	url(r'^sign_up/', views.sign_up , name='sign_up'),
	url(r'^create/$', views.create_project, name='create_project'),
	url(r'^create_task/(?P<pk>[0-9]+)/$', views.create_task, name='create_task'),
	url(r'^project/(?P<pk>[0-9]+)/$', views.project_detail, name='project_detail'),
	url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]