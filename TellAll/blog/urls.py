from django.conf.urls import url, include
from blog import views

urlpatterns = [
    url(r'^$', views.BlogPostListView.as_view(), name='blog_post_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/update-post/$', views.BlogPostUpdateView.as_view(), name='edit_blog_post'),
    url(r'^post/(?P<pk>\d+)/remove-post/$', views.BlogPostDeleteView.as_view(), name='delete_blog_post'),
    url(r'^draft-posts/$', views.DraftListView.as_view(), name='draft_posts'),
    url(r'^post/(?P<pk>\d+)/new-comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve-comment/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove-comment/$', views.comment_remove, name='remove_comment'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
]