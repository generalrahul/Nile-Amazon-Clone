from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from .forms import ProductForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(DetailView):
  model = Product  # Specify the model to fetch data from
  template_name = 'products/product_detail.html'  # Template to render
  context_object_name = 'product'  # Name used to access the product object in the template

class ProductCreateView(CreateView):
  model = Product
  form_class = ProductForm
  template_name = 'products/add_product.html'  # Replace with your template path
  success_url = reverse_lazy('products-page')  # Replace 'product-list' with your product list URL name

def product_list(request):
  products = Product.objects.all()
  return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
  product = Product.objects.get(id=product_id)
  return render(request, 'product_detail.html', {'product': product})

def add_product(request):
  if request.method == 'POST':
    form = ProductForm(request.POST, request.FILES)  # Handle uploaded files in request.FILES
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/products/')
  else:
    form = ProductForm()

  return render(request, 'add_product.html', {'form': form})
