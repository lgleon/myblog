from django.conf.urls import url
from django.urls import path
from .views import get_posts, post_detail, create_or_edit_post

#I don't need to put like views.get_post because I imported the views
urlpatters = [
    path('', get_posts, name='get_posts'),
    path('', post_detail, name='post_detail'),
    path('', create_or_edit_post, name='new_post'),
    path('', create_or_edit_post, name='edit_post'),
]