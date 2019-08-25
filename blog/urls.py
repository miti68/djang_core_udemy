
from django.conf.urls import url
from .views import (
    post_model_list_view,
    post_model_detail_view,
    post_model_create_view,
    post_model_update_view,
    post_model_delete_view,
    )
app_name = 'blog'
urlpatterns = [
    url(r'^$', post_model_list_view, name='list'),
    url(r'^create/$', post_model_create_view, name='create'),
    url(r'^(?P<id>\d+)/$', post_model_detail_view, name='detail'), #id is keyword argument -> pass to HttpRequest
    url(r'^(?P<id>\d+)/edit/$', post_model_update_view, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_model_delete_view, name='delete'),
]
