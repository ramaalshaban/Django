from django.urls import path
from . import views
from .views import PostListView
urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    # when we use class based views
    # we cant pass in the class just simply by passing the name
    # it has to be converted into an actual view 
    # So we add as_view() "rhe parantes means executing the thing."
    path('about/', views.about, name='blog-about'),\


]

# by default class based views looks for templates of a certin naming pattern
# <app>/<model>_<viewtype>.html : blog/post_list.html
# but we can change what template that we want to use


