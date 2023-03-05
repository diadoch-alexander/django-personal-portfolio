
from django.urls import path
from blog.views import all_blogs,show_blog

app_name='blog'

urlpatterns = [
    path('',all_blogs,name='all_blogs'),
    path('<int:blog_id>',show_blog,name='show_blog'),

]