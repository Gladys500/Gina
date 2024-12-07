
from django.contrib import admin
from django.urls import path
from GinaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('starter/', views.starter,name='starter'),
    path('about/', views.about,name='about'),
    path('booking/', views.booking,name='booking'),
    path('Chefs/', views.chefs_page,name='Chefs'),
    path('contact/', views.contact,name='contact'),
    path('events/', views.events,name='events'),
    path('gallery/', views.gallery,name='gallery'),
    path('menu/', views.menu,name='menu'),
    path('testimonials/', views.testimonials,name='testimonials'),
]
