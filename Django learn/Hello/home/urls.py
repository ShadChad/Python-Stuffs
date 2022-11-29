from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("", views.index, name = 'home'),
   path("about", views.about, name = 'about'),
   path("services", views.services, name = 'services'),
   path('contact', views.contact, name = "contact"),
   path('vanilla', views.vanilla, name = "vanilla"),
   path('icecream', views.ice, name = "ice"),
   path('req', views.req, name = 'req.html'),
   path('checkout', views.checkout, name = 'checkout'),
]