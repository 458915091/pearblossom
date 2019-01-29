from django.urls import path
from .views import * 

app_name = 'blog'
urlpatterns = [
    path('home/', home, name='home'),
    path('<str:author>/<int:num>', detail, name='detail'),
    path('add/', add, name='add'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('center/', center, name='center'),
]