from django.shortcuts import render
from products.models import Product


def get_products(request, slug):
      
    try:
        product = Product.objects.get(slug=slug)
        context = {'product': product}

        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_by_size(size)
            context['updated_price'] = price
            context['selected_size'] = size

        return render(request, 'product/product.html', context)
    except Exception as e:
        print(e)
