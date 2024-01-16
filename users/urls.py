from django.urls import path
from . import views

urlpatterns = [
    path('seller_registration/', views.seller_registration, name='seller_registration'),
    path('buyer_registration/', views.buyer_registration, name='buyer_registration'),
    # Add other URLs as needed
    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
]