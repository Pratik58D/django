from django.contrib import admin
from django.urls import path
from django.urls import include
from home import views

#django admin header customization
admin.site.site_header = "Admin Pratik Devkota"
admin.site.site_title = "Welcome to admins Dashboard "
admin.site.index_title = "Welcome to this Portal"



urlpatterns = [
    path('', views.home ,name= "home"),
    path('about', views.about ,name= "about"),
    path('contact', views.contact ,name= "contact"),
    path('projects/', views.projects ,name= "projects"),
    
]
