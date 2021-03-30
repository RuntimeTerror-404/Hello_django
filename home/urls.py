from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('services', views.services, name = 'services') ,
    path("contacts", views.contacts, name = "contacts"),
    path("hello", views.hello, name = "hello"),
    path("about", views.about, name = "about"),
    path("stall", views.stall, name = "stall"),
    path("online", views.online, name = "online"),
    path("homepage", views.homepage, name = "homepage")

]