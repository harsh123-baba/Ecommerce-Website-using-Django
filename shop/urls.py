from django.contrib import admin
from django.urls import path, include
from shop import views
from django.conf.urls import url
from . import views

app_name = 'shop'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('prodview/<int:myid>/', views.prodview, name = 'prodview'),
    path('update_item/',views.updateItem, name = 'item'),
    path('cart/' , views.cart, name = 'cart'),
    path('checkout/', views.checkout , name ='checkout')

    
]
