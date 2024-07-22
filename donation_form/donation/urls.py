# donation/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donate, name='donate'),
    path('confirmation/', views.donation_confirmation, name='donation_confirmation'),
    path('view/', views.view_donations, name='view_donations'),
]
