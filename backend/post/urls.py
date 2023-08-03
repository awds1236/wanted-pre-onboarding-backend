from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.index, name='post'),
    path('posting', views.posting, name='posting'),
    path('<int:pk>', views.post_detail, name='post_detail'),   
    path('post/delete/<int:post_id>/', views.delete_post, name='post_delete'),    
    path('edit/<int:post_id>/', views.post_edit, name='post_edit'),

]