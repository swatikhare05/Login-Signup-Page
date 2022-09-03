from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('uregister', views.uregister,name='uregister'),
    path('ulogin', views.ulogin,name='ulogin'),
    path('ulogout', views.ulogout,name='ulogout'),
    
]
