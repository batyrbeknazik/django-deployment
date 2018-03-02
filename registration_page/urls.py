
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^registration',views.registration,name='registration'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^logout/$', views.user_logout, name='logout')

]