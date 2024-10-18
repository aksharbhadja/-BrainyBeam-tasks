from django.shortcuts import render
from django.db.models import Q
from .models import Product

def product_list(request):
    # Get min_price and max_price from the request (query parameters)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Start with an empty filter
    filters = Q()

    # If the minimum price is provided, apply it to the filter
    if min_price:
        filters &= Q(price__gte=min_price)

    # If the maximum price is provided, apply it to the filter
    if max_price:
        filters &= Q(price__lte=max_price)

    # Get products based on the dynamic filters
    products = Product.objects.filter(filters)

    return render(request, 'shop/product_list.html', {'products': products})

