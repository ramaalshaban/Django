from django.urls import path
from . import views
from .views import PostListView, PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    # when we use class based views
    # we cant pass in the class just simply by passing the name
    # it has to be converted into an actual view
    # So we add as_view() "rhe parantes means executing the thing."
    path('about/', views.about, name='blog-about'),
    # here i will try to crate a url pattern that includes a variable
    # pk is the primary key of the post and what kind of variable
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # so we grap th pk info from the url and use it in our view
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    # the form name i will create for this one wil lbe named like post_form as a temolate
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(success_url= '/'), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

]

# by default class based views looks for templates of a certin naming pattern
# <app>/<model>_<viewtype>.html : blog/post_list.html
# but we can change what template that we want to use
