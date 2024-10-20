from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product

def product_list(request):
    query = request.GET.get('q', '')  # To Get search query 
    products = Product.objects.filter(name__icontains=query) if query else Product.objects.all()

    paginator = Paginator(products, 10)  # To Show 10 products per page
    page_number = request.GET.get('page')  # To Get the page number 
    page_obj = paginator.get_page(page_number)  # To Get the products 

    context = {
        'page_obj': page_obj,
        'query': query,  # To keep the search query in the form
    }
    return render(request, 'myapp/product_list.html', context)
