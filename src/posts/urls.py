from django.urls import re_path

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
)

app_name = "posts"

urlpatterns = [
	re_path(r'^$', post_list, name='list'),
	re_path(r'^create/$', post_create, name='create'),
	re_path(r'^(?P<id>\d+)/$', post_detail, name='detail'),
	re_path(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
	re_path(r'^(?P<id>\d+)/delete/$', post_delete, name='delete'),
]

