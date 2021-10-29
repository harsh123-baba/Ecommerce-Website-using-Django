from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),

]
