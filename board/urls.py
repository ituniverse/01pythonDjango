from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.board_list, name='board_list'),
    url(r'^board/(?P<pk>[0-9]+)/$', views.board_detail, name='board_detail'),
    url(r'^board/new/$', views.board_new, name='board_new'),
    url(r'^board/(?P<pk>[0-9]+)/edit/$', views.board_edit, name='board_edit'),
    url(r'^drafts/$', views.board_draft_list, name='board_draft_list'),
    url(r'^board/(?P<pk>\d+)/publish/$', views.board_publish, name='board_publish'),
    url(r'^board/(?P<pk>\d+)/remove/$', views.board_remove, name='board_remove'),

    url(r'^board/(?P<pk>\d+)/comment/$', views.add_board_comment, name='add_board_comment'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]












