from django.urls import path
from .views import login_view,show_token

app_name = 'login'
urlpatterns = [
    path('', login_view, name='login'),
    path('show_token',login_view,name='show_token')
]
