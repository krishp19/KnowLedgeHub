from django.urls import path,include
from .views import HomeView,ArticleDetailViews,AddpostView,UpdatePostView,DeletePostView,AddcommentView,BlogView,BlogDetailViews,LikeView
from members.views import UserRegisterView

urlpatterns = [
    path('',UserRegisterView.as_view(),name="register"),
    path('home/',HomeView.as_view(),name="home"),
    path('blogs/',BlogView.as_view(),name="blog"),
    path('blog/<int:pk>',BlogDetailViews.as_view(),name="blog-detail"),
    path('article/<int:pk>', ArticleDetailViews.as_view(),name = 'article-detail'),
    path('add_post/',AddpostView.as_view(),name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name = 'update_post'),
    path('article/delete/<int:pk>/remove',DeletePostView.as_view(),name = 'delete_post'),
    path('article/<int:pk>/comment/',AddcommentView.as_view(),name='add_comment'),
    path('like/<int:pk>', LikeView, name='like_post'),

]

