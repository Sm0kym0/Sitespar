from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stores/', views.store_list, name='stores'),
    path('catalog/', views.product_list, name='catalog'),
path('about/', views.about, name='about'),
path('contacts/', views.contacts, name='contacts'),


]
