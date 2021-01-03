"""Defines URL patterns for blogs"""
from django.urls import path
from . import views

from django.views.generic import TemplateView

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for adding a new blog
    path('new_blog/', views.new_blog, name='new_blog'),
    # Page for editting an entry.
    path('edit_blogpost/<int:blog_id>/', views.edit_blogpost, name='edit_blogpost'),
    # not allow
    # path('blogs/not_allow/', views.index, name='not_allow')
    path('not_allow', TemplateView.as_view(template_name='not_allow.html'), name='not_allow'),
]