from django.urls import path
from . import views

urlpatterns = [
    path('phonex/', views.phonex, name='phonex'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    path('phones/', views.phones, name='phones'),
    path('Login/', views.Login, name='Login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('sellphone/', views.sellphone, name='sellphone'),
    
    
    
   
]