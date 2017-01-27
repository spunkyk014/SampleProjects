from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'URLShortener'
urlpatterns = [
    #ex: /URLShortener/
    url(r'^$', views.UserList, name='userlist'),
    url(r'^userlist/$', views.UserList, name='userlist'),
    url(r'^URLs/(?P<pk>\w+\d*)/createURL/$', views.URLCreateView.as_view(), name='urlcreate'),
    url(r'^URLs/(?P<user_id>\w+\d*)/(?P<pk>\w+\d*)/deleteURL/$', views.URLDeleteView.as_view(), name='urldelete'),
    url(r'^URLs/(?P<pk>\w+\d*)', views.UserURLDetail, name='userurls'),
    url(r'^URLs/$', views.UserHomeRedirect, name='user_home'),

]    

urlpatterns += staticfiles_urlpatterns()