
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('home.html', views.home, name='home'),

  path('contact.html', views.contact, name='contact'),
  path('price.html', views.price, name='price'),
  path('about.html', views.about, name='about'),
  path('service.html', views.service, name='service'),
  path('appointment.html', views.appointment, name='appointment'),
 
 
 




]