from django.urls import path

from .import views

app_name='ecommerceadmin'

urlpatterns = [
    path('home',views.index,name='adminhome'),
    path('',views.login,name='login'),
    path('catalogue',views.catalogue,name='catalogue'),
    path('addproduct',views.add_product,name='add_product'),
    path('updatestock',views.update_stock,name='update_stock'),
    path('orderhistory',views.order_history,name='order_history'),
    path('customers',views.customers,name='customers'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),

    path('change_password',views.change_password,name='change_password'),





]