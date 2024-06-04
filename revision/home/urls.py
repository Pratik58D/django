from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    #path('boy', views.home , name = "home"),
    #path("", views.contact, name="contact"),
    #path("invent", views.name, name = "Name")
    
    path("", views.home , name= "home"),
    path("contacts", views.contact , name= "contact"),
    path("projects", views.projects, name= "projects"),
    path("about", views.about , name= "about")
]
