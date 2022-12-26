from django.urls import path

from .import views

app_name='common'

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('shop',views.shop,name='shop'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),



    
]


