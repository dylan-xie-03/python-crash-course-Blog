from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogPostForm




# Create your views here.
def index(request):
    """The home page for blogs"""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)


@login_required
def new_blog(request):
    """Add a new blog."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')    # redirect to home page

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


@login_required
def edit_blogpost(request, blog_id):
    """Edit an existing blog."""

    blog = BlogPost.objects.get(id=blog_id)
    if blog.owner == request.user:
        if request.method != 'POST':
            # Initial request; pre-fill form with the current blog.
            form = BlogPostForm(instance=blog)
        else:
            # POST data submitted; process data.
            form = BlogPostForm(instance=blog, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('blogs:index')

        context = {'blog': blog, 'form': form}
        return render(request, 'blogs/edit_blogpost.html', context)
    else:
        return redirect('blogs:not_allow')




