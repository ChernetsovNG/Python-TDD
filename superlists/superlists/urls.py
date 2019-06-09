from django.conf.urls import url

from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/one-unique-list-in-the-world/$', views.view_list, name='view_list'),
]
