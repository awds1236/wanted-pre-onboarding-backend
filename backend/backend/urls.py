from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import path, include


urlpatterns = [
   path('', include('main.urls')),
   path("admin/", admin.site.urls),
   path('join/', include('join.urls')),
   path('login/', include('login.urls'),name='login'),
   path('post/',include('post.urls')),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
