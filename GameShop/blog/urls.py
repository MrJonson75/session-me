from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_platform, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('post/<slug:post_slug>', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', views.GameCategory.as_view(), name='category'),
    path('edit_page/<slug:slug>', views.UpdatePage.as_view(), name='edit_page'),
]