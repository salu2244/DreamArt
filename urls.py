"""
URL configuration for Dream_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Dream_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contact/', views.contact, name="contact"),
    path('newproject/', views.newproject, name="newproject"),
    path('adminhome/', views.adminHome, name="adminhome"),
    path('admindashboard/', views.admin_dashboard, name="admindashboard"),
    path('add-category/', views.add_category, name="add_category"),
    path('view-category/', views.view_category, name="view_category"),
    path('edit-category/<int:pid>/', views.edit_category, name="edit_category"),
    path('delete-category/<int:pid>/', views.delete_category, name="delete_category"),
    path('add-product/', views.add_product, name='add_product'),
    path('view-product/', views.view_product, name='view_product'),
    path('edit-product/<int:pid>/', views.edit_product, name="edit_product"),
    path('delete-product/<int:pid>/', views.delete_product, name="delete_product"),
    path('manage-feedback/', views.manage_feedback, name="manage_feedback"),
    path('delete-feedback/<int:pid>/', views.delete_feedback, name="delete_feedback"),
    path('feedback-read/<int:pid>/', views.read_feedback, name="read_feedback"),
    path('manage-order/', views.manage_order, name="manage_order"),
    path('delete-order/<int:pid>/', views.delete_order, name="delete_order"),
    path('admin-order-track/<int:pid>/', views.admin_order_track, name="admin_order_track"),
    path('manage-user/', views.manage_user, name="manage_user"),
    path('delete-user/<int:pid>/', views.delete_user, name="delete_user"),
    path('payment/', views.payment, name="payment"),
    path('user-product/<int:pid>/', views.user_product, name="user_product"),
    path('product-detail/<int:pid>/', views.product_detail, name="product_detail"),
    path('booking/', views.booking, name="booking"),
    path('add-to-cart/<int:pid>/', views.addToCart, name="addToCart"),
    path('cart/', views.cart, name="cart"),
    path('incredecre/<int:pid>/', views.incredecre, name="incredecre"),
    path('deletecart/<int:pid>/', views.deletecart, name="deletecart"),
    path('user-feedback/', views.user_feedback, name="user_feedback"),
    path('product-detail/<int:pid>/', views.product_detail, name="product_detail"),
    path('registration/', views.registration, name="registration"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logoutuser, name="logout"),
    path('change-password/', views.change_password, name="change_password"),
    path('my-order/', views.myOrder, name="myorder"),
    path('user-order-track/<int:pid>/', views.user_order_track, name="user_order_track"),
    path('change-order-status/<int:pid>/', views.change_order_status, name="change_order_status"),
    path('admin-change-password/', views.admin_change_password, name="admin_change_password"),
]

