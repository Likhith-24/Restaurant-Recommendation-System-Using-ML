from django.contrib import admin
from django.urls import path
from restaurant import views

urlpatterns = [

    path('',views.home, name= 'base'),      
    path("home",views.home,name='home'),
    path("recommend",views.recommend,name="recommend"),
    path("search",views.search,name="search"),
    path("restaurant",views.restaurant,name="restaurant"),

    path('signup',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout',views.LogoutPage,name='logout'),
   
    path('card/<int:id>/', views.card, name='card'),
    path('carthome',views.carthome,name='carthome'),
     path('cart/<int:id>/',views.cart,name='cart'),
     path("clear",views.clear,name="clear"),

    path("placeorder/<int:id>/",views.placeorder,name="placeorder"),
    path("order",views.placeorderhome,name="placeorderhome"),
    path("removeorder/<int:id>/",views.removeorder,name="placeorderhome"),

]