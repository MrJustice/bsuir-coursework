from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('user/<str:pk>/', views.user, name='user'),
    path('product/<str:pk>/', views.product, name='product'),
    path('feedback/', views.feedback, name='feedback'),
    path('guarantees/', views.guarantees, name='guarantees')
]