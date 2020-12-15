from . import views
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as vws

urlpatterns = [
    path('', views.index, name='home'),
    path('registration/', views.registration, name='registration'),
    path('login/', vws.LoginView.as_view(), name='login'),
    path('logout/', vws.LogoutView.as_view(), name='logout'),
    path('catalog/', views.catalog, name='catalog'),
    path('user/<str:pk>/', views.user, name='user'),
    path('product/<str:pk>/', views.product, name='product'),
    path('create_order/<str:pk>', views.create_order, name='create_order'),
    path('guarantees/', views.guarantees, name='guarantees'),
]