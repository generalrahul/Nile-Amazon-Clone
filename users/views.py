from django.shortcuts import render, redirect
from .forms import SellerRegistrationForm, BuyerRegistrationForm
from django.contrib.auth.decorators import login_required
from products.models import Product

def seller_registration(request):
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            form.save()
            return redirect('seller_dashboard')  # Redirect to seller dashboard
    else:
        form = SellerRegistrationForm()
    return render(request, 'seller_registration.html', {'form': form})

def buyer_registration(request):
    if request.method == 'POST':
        form = BuyerRegistrationForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            form.save()
            return redirect('buyer_dashboard')  # Redirect to buyer dashboard
    else:
        form = BuyerRegistrationForm()
    return render(request, 'buyer_registration.html', {'form': form})

@login_required
def seller_dashboard(request):
    # Get seller-specific data or perform necessary operations
    # For example, fetch and display the seller's products
    seller_products = Product.objects.filter(seller=request.user)

    return render(request, 'seller_dashboard.html', {'seller_products': seller_products})