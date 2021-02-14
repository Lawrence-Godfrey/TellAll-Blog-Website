from django.conf.urls import url, include
from blog import views

urlpatterns = [
    url(r'^$', views.BlogPostListView.as_view(), name='blog_post_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)$', views.BlogPostDetailView.as_view(), name='blog_post_detail'),
    url(r'^post/new-post/$', views.CreateBlogPostView.as_view(), name='new_blog_post'),
    url(r'^post/(?P<pk>\d+)/update-post/$', views.BlogPostUpdateView.as_view(), name='edit_blog_post'),
    url(r'post/(?P<pk>\d+)/remove-post/$', views.BlogPostDeleteView.as_view(), name='delete_blog_post'),
    url(r'^draft-posts/$', views.DraftListView.as_view(), name='draft_posts'),
    url(r'^post/(?P<pk>\d+)/new-comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve_comment/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove_comment/$', views.comment_remove, name='remove_comment'),
    url(r'^post/(?P<pk>\d+)/publish_post$', views.publish_blog_post, name='publish_post')
]