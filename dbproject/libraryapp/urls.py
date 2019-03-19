from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', login, {'template_name': 'libraryapp/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'libraryapp/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^borrow/(?P<copy_id>[0-9]+)/$', views.borrow, name='borrow'),
    url(r'^mybook/$', views.mybook, name='mybook'),
    url(r'^return/(?P<bor_id>[0-9]+)/$', views.retbook, name='return'),
    url(r'^search/', views.search, name='search'),
]
