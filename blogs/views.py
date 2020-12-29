from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def index(request):
    """The home page for blogs"""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs':blogs}
    return render(request, 'blogs/index.html', context)

def new_blog(request):
    """Add a new blog."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')    # redirect to home page

    context = {'form':form}
    return render(request, 'blogs/new_blog.html', context)

# def blogpost(request, blogpost_id):
#     """Edit an existing blog."""
#     blogpost = BlogPost.objects.get(id=blogpost_id)
#
#     if request.method != 'POST':
#         #Initial request; pre-fill form with the current blog.
#         form = BlogPostForm(instance=blogpost)
#     else:
#         # POST data submitted; process data.
#         form = BlogPostForm(instance=blogpost, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('blogs:index', blogpost_id = blogpost.id )
#
#         context = {'blogpost':blogpost, 'form':form}
#         return render(request, 'blogs/blogpost.html', context)

# it's very possible to be wrong

def edit_blogpost(request, blog_id):
    """Edit an existing blog."""
    blog = BlogPost.objects.get(id=blog_id)

    if request.method != 'POST':
        #Initial request; pre-fill form with the current blog.
        form = BlogPostForm(instance=blog)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index', blog_id = blog.id )

        context = {'blog':blog, 'form':form}
        return render(request, 'blogs/edit_blogpost.html', context)

# def blogpost(request, blogpost_id):
#     """Show a single topic and all its entries"""
#     blogpost = BlogPost.objects.get(id=blogpost_id)
#     context = {'blogpost':blogpost}
#     return render(request, 'blogs/blogpost.html', context)


