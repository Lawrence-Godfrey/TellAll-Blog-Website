from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from blog.models import *
from blog.forms import *


class AboutView(TemplateView):
    template_name = 'about.html'


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'

    def get_queryset(self):
        return BlogPost.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')         # __lte = <=   |  - infront of published_date orders by descending


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'


class CreateBlogPostView(LoginRequiredMixin, CreateView):
    model = BlogPost
    login_url = '/login/'
    template_name = 'blog/post_form.html'
    redirect_field_name = 'blog/post_detail.html'

    form_class = BlogPostForm


class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = BlogPostForm


class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/blogpost_list.html'
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__isnull=True).order_by('created_date')


################### Function Views #####################

@login_required
def publish_blog_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', pk=post.pk)

        else:
            form = CommentForm()

        return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()

    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()

    return redirect('post_detail', pk=post_pk)